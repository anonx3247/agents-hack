import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from smolagents import ToolCallingAgent, tool, WikipediaSearchTool, LiteLLMModel
# Add this import for Claude Sonnet 4 model integration
# from smolagents import LiteLLMModel
from agents.memory_agent import update_memory
from agents.exercise_trainer_agent import ExerciseTrainerAgent, Exercise
from agents.exercise_summarizer import summarize_exercises
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize ChromaDB connection
embeddings = HuggingFaceEmbeddings(model_name=os.getenv("EMBEDDING_MODEL"))
problems_db = Chroma(
    collection_name="pb_solutions",
    embedding_function=embeddings,
    persist_directory=os.getenv("CHROMA_DB_DIR")
)
notes_db = Chroma(
    collection_name="class-notes",
    embedding_function=embeddings,
    persist_directory=os.getenv("CHROMA_DB_DIR")
)

AGENT_SYSTEM_PROMPT = """
You are Gauss, a specialized STEM learning assistant for students. You are helpful, patient, and always take a step-by-step approach to teaching. Your goal is to help students truly understand concepts, not just get answers.

Guidelines:
- For general questions about theorems, scientific principles, or when the student asks about topics beyond the basic coursework, use the Wikipedia tool.
- For questions about classwork, assignments, or anything covered in the course, use the documentation and class notes tools.
- When the student asks to practice or train, use the exercise search tool. Always ask if they want to practice more exercises after giving one.
- When the student wants to train on a specific exercise, use the 'train_on_exercise' tool to launch a dedicated training session. In this session, guide the student through the exercise step by step, asking probing questions and encouraging them to think. Do not reveal the answer unless the student is truly stuck and requests it as a last resort.
- You are initialized with a summary of previous interactions (memory_summary) and should use this to personalize your help. You do not need to call a memory tool for this.
- Always be encouraging, supportive, and adapt your explanations to the student's level.
- Never give away answers immediately. Instead, break down problems, ask guiding questions, and help the student build understanding incrementally.
- If the student is struggling, offer hints or break the problem into smaller parts.
- Only provide the final answer if the student insists or is unable to proceed after multiple hints.

DO NOT TRAIN ON A SPECIFIC EXERCISE BEFORE THE STUDENT HAS ASKED TO DO SO.
DO NOT USE THE DOCUMENTATION TOOL UNLESS THE STUDENT HAS ASKED A QUESTION ABOUT THE COURSE.
DO NOT USE THE EXERCISE SEARCH TOOL UNLESS THE STUDENT HAS ASKED TO PRACTICE.
DO NOT USE THE WIKIPEDIA TOOL UNLESS THE STUDENT HAS ASKED A QUESTION ABOUT A TOPIC NOT COVERED IN THE COURSE.
"""

@tool
def doc_research(query: str) -> str:
    """
    Search documentation and class notes to answer a student's question.
    
    Args:
        query (str): The student's question or topic to research
        
    Returns:
        str: The research results from documentation and class notes
    """
    # Search for relevant content in class notes
    results = notes_db.similarity_search(query, k=10)
    
    if not results:
        return "I couldn't find any relevant information in the class notes."
    
    # Format the results
    formatted_results = []
    for i, doc in enumerate(results, 1):
        formatted_results.append(f"Result {i}:\n{doc.page_content}\n")
    
    return "Here's what I found in the class notes:\n\n" + "\n".join(formatted_results)

@tool
def exercise_search(topic: str, problem_types: list = None) -> str:
    """
    Find and recommend exercises/problems for a given topic. Fetches 10 results and selects the best to present to the user. Always ask if they want to practice more after giving one.
    
    Args:
        topic (str): The topic or subject area to find exercises for
        problem_types (list, optional): A list of accepted `problem_type` values to filter on (e.g., ["Geometry", "Algebra"]). If provided, only exercises with matching problem_type will be considered.
        
    Returns:
        str: A recommended exercise and prompt asking if the user wants more practice
    """
    # Prepare filter dictionary if problem_types are provided
    filter_dict = {}
    if problem_types:
        # Chroma ne supporte pas directement les OR dans une liste -> on boucle plus tard si nécessaire
        # ici on prend le cas simple : un seul type
        if len(problem_types) == 1:
            filter_dict = {"problem_type": problem_types[0]}
        else:
            or_list = [{"problem_type": pt} for pt in problem_types]
            filter_dict = {"$or": or_list}

    # Search for relevant exercises using vector similarity
    results = problems_db.similarity_search(topic, k=10, filter=filter_dict if filter_dict else None)
    
    # Create exercise IDs and content pairs for summarization
    exercise_pairs = [(f"ex_{i+1}", doc.page_content) for i, doc in enumerate(results)]
    
    # Get summarized titles for all exercises
    summarized_exercises = summarize_exercises(exercise_pairs)
    
    # Format the exercises with their titles
    formatted_exercises = []
    for i, (ex_id, title) in enumerate(summarized_exercises):
        doc = results[i]
        meta_lines = "\n    ".join([f"{key}: {value}" for key, value in doc.metadata.items()])
        formatted = f"{i+1}. [id: {ex_id}] {title}\n    {meta_lines}"
        formatted_exercises.append(formatted)
    
    return f"Relevant exercises:\n{formatted_exercises}"

@tool
def train_on_exercise(exercise_id: str) -> str:
    """
    Launch a guided, step-by-step training session with the student on the given exercise. Do not reveal the answer unless the student is truly stuck and requests it as a last resort. Guide the student slowly, asking questions and providing hints as needed.
    
    Args:
        exercise_id (str): The ID of the exercise to work through with the student
        
    Returns:
        str: Initial prompt to start the guided training session
    """
    
    trainer = ExerciseTrainerAgent(exercise_id=exercise_id)
    return trainer.run()

def save_memories() -> str:
    """
    Delegate to the summary agent to summarize the conversation and update the memory file.
    
    Returns:
        str: Confirmation message indicating successful memory update
    """
    # Write the conversation to messages and get the summary
    conversation = agent.write_memory_to_messages()
    update_memory(conversation)
    return f"Conversation processed and memory updated successfully."


class STEMLearningAgent(ToolCallingAgent):
    """
    Specialized agent to help STEM students learn better.
    Features:
    - Doc research (RAG)
    - Exercise search (with selection loop)
    - Wikipedia search (via built-in tool)
    """

    def __init__(self, memory_summary: str = "", *args, **kwargs):
        """
        Initialize the STEM Learning Agent.
        
        Args:
            memory_summary (str, optional): Summary of previous interactions. Defaults to "".
            *args: Additional positional arguments for MultiStepAgent
            **kwargs: Additional keyword arguments for MultiStepAgent
        """
        # Set Claude Sonnet 4 as the model
        model = LiteLLMModel(
            model="claude-opus-4-20250514",
            api_key="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"
        )
        
        tools = [
            doc_research,
            exercise_search,
            train_on_exercise,
            WikipediaSearchTool(
                user_agent="STEMLearningAgent (your@email.com)",
                language="en",
                content_type="summary",
                extract_format="WIKI"
            )
        ]

        self.memory_summary = memory_summary
        
        super().__init__(
            tools=tools, 
            model=model,
            *args, 
            **kwargs
        )

        

    def initialize_system_prompt(self) -> str:
        """
        Initialize the system prompt for the agent.
        
        Returns:
            str: The system prompt
        """
        return AGENT_SYSTEM_PROMPT + f"\nPrevious conversation: {self.memory_summary}\n"
    
    def run(self, user_input: str) -> str:
        """
        Run the agent with the given user input.
        
        Args:
            user_input (str): The user's input
            
        Returns:
            str: The agent's response
        """
        print("\n🤔 Thinking...")
        return super().run(user_input)

# Example instantiation (customize as needed)
if __name__ == "__main__":
    # Initialize the agent with empty memory
    agent = STEMLearningAgent()
    
    print("🤖 Welcome to Gauss, your STEM learning assistant!")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check for exit command
        if user_input.lower() in ['exit', 'quit']:
            save_memories()
            print("\nGoodbye! Have a great day of learning! 👋")
            break
            
        try:
            # Get agent's response
            response = agent.run(user_input)
            
            # Print the response
            print("\nGauss:", response)
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            
    # Save the conversation memory before exiting
    try:
        print("\n💾 Saving conversation memory...")
        agent.save_memories()
    except Exception as e:
        print(f"\n⚠️ Warning: Could not save conversation memory: {str(e)}")
