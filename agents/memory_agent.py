from smolagents import CodeAgent, tool, LiteLLMModel
import os
import datetime

MEMORY_AGENT_PROMPT = """
You are a memory agent for a STEM learning assistant. Your job is to maintain a concise memory file for each student, which will be used to personalize future interactions.

Your responsibilities:
- Summarize each conversation, focusing on:
    - What the student struggled with
    - What topics were covered
    - What exercises/problems were attempted or seen
    - What the student learned or improved on
- Keep the memory file concise and relevant:
    - Include general background on the student's level and what they are learning
    - Include the latest topics and exercises the student has worked on
    - Include summaries of the last few conversations (not all history)
    - If the file gets too long, rewrite it to keep only the most important and recent information
- If the memory file is empty, try to infer or ask for the student's background and current learning topics.
"""

memory_file = "student_memory.md"  # You can customize this path as needed

model = LiteLLMModel(
    model="claude-3-5-haiku-20241022",
    api_key="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"
)

def summarize_conversation(conversation: str) -> str:
    """
    Generate a concise memory of a student conversation, highlighting key learning points and challenges.
    
    Args:
        conversation (str): The complete conversation text to be analyzed
        
    Returns:
        str: A structured memory containing:
            - Student's struggles and challenges
            - Topics covered in the session
            - Exercises or problems attempted
            - Learning outcomes and improvements
    """
    prompt = f"""Please summarize this conversation, focusing on:
1. What the student struggled with
2. What topics were covered
3. What exercises/problems were attempted or seen
4. What the student learned or improved on

Conversation:
{conversation}

Provide a concise memory that captures the key points."""
    messages = [
        {
            "role": "system",
            "content": MEMORY_AGENT_PROMPT
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    return model.generate(messages).content

def summarize_memory(memory: str) -> str:
    """
    Condense the student's memory file while preserving critical learning information.
    
    Args:
        memory (str): The current memory file content to be condensed
        
    Returns:
        str: A condensed version of the memory file containing:
            - Student's learning background and current topics
            - Recent challenges and progress
            - Latest covered material and exercises
            - Key learning achievements
    """
    prompt = f"""Please condense this memory file while preserving the most important information about:
1. Student's background and current learning topics
2. Recent struggles and improvements
3. Latest topics and exercises covered
4. Key learning outcomes

Memory content:
{memory}

Provide a concise memory that maintains the essential information."""
    messages = [
        {
            "role": "system",
            "content": MEMORY_AGENT_PROMPT
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    return model.generate(messages).content

def read_memory() -> str:
    """
    Retrieve the current contents of the student's memory file.
    
    Returns:
        str: The complete contents of the memory file if it exists,
             an empty string if the file doesn't exist
    """
    if not os.path.exists(memory_file):
        return ""
    with open(memory_file, "r") as f:
        return f.read()

def write_memory(content: str) -> str:
    """
    Update the student's memory file with new content.
    
    Args:
        content (str): The new content to write to the memory file
        
    Returns:
        str: Confirmation message indicating successful update
    """
    with open(memory_file, "w") as f:
        f.write(content)
    return "Memory file updated."

def update_memory(conversation: str):
    """
    Process and store a new conversation in the student's memory file.
    
    Args:
        conversation (str): The conversation to be summarized
        
    Process:
        1. Reads and summarizes the latest conversation
        2. Adds timestamp to the memory
        3. Manages memory file size by condensing if necessary
        4. Updates the memory file with the new memory
    """
    # 1. Read the latest conversation
    # 2. Summarize it
    memory = summarize_conversation(conversation)
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    dated_memory = f"[{date_str}]\n{memory}"

    # 3. Read the memory file
    memory = read_memory()

    # 4. If memory file > 2000 chars, condense it
    if len(memory) > 2000:
        print("Memory file too long, condensing...")
        condensed = summarize_memory(memory)
        memory = f"[Condensed on {date_str}] {condensed}"

    # 6. Append the memory of last interaction to the file
    updated_memory = (memory + "\n" + dated_memory).strip() if memory else dated_memory
    write_memory(updated_memory)
    print("Memory file updated.")