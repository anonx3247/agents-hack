from smolagents import MultiStepAgent, tool, WikipediaSearchTool, LiteLLMModel
# Add this import for Claude Sonnet 4 model integration
# from smolagents import LiteLLMModel
from agents.summary_agent import update_memory
from agents.exercise_trainer_agent import ExerciseTrainerAgent, Exercise

# Placeholder imports for ChromaDB and memory handling
# from chromadb import Client as ChromaClient
# import memory_utils

# Initialize connections to your vector DBs and memory file here
# notes_db = ChromaClient(...)
# docs_db = ChromaClient(...)
# problems_db = ChromaClient(...)
# memory_file = 'path/to/memory.json'

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
    # TODO: Implement RAG search over docs_db and notes_db
    return "[Doc research result placeholder]"

@tool
def exercise_search(topic: str) -> str:
    """
    Find and recommend exercises/problems for a given topic. Fetches 10 results and selects the best to present to the user. Always ask if they want to practice more after giving one.
    
    Args:
        topic (str): The topic or subject area to find exercises for
        
    Returns:
        str: A recommended exercise and prompt asking if the user wants more practice
    """
    # TODO: Fetch 10 exercises from problems_db
    exercises = [f"Exercise {i+1} for {topic}" for i in range(10)]  # Placeholder
    # TODO: Implement selection logic (e.g., based on difficulty, relevance, or user history)
    selected = exercises[0]  # Placeholder: select the first one
    # In a real implementation, you might return a list or ask the user to choose
    return f"Recommended exercise: {selected}\nWould you like to practice more exercises?"

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

@tool
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

class STEMLearningAgent(MultiStepAgent):
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
            save_memories,
            WikipediaSearchTool(
                user_agent="STEMLearningAgent (your@email.com)",
                language="en",
                content_type="summary",
                extract_format="WIKI"
            )
        ]
        
        super().__init__(
            tools=tools, 
            model=model, 
            prompt_templates={"system": AGENT_SYSTEM_PROMPT + f"\nPrevious conversation: {memory_summary}\n"},
            *args, 
            **kwargs
        )
        self.memory_summary = memory_summary

agent = STEMLearningAgent()

# Example instantiation (customize as needed)
if __name__ == "__main__":
    agent = STEMLearningAgent(memory_summary="Student struggled with integrals last session.")
    # Example: agent.run() or integrate with your server framework
