from smolagents import Agent, tool, LiteLLMModel
import os
import datetime

SUMMARY_AGENT_PROMPT = """
You are a summary agent for a STEM learning assistant. Your job is to maintain a concise memory file for each student, which will be used to personalize future interactions.

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

MEMORY_FILE_PATH = "student_memory.json"  # You can customize this path as needed

class SummaryAgent(Agent):
    """
    Agent to summarize student conversations and manage the memory file for future personalization.
    """
    def __init__(self, memory_file: str = MEMORY_FILE_PATH, *args, **kwargs):
        # Set Claude Sonnet 4 as the model
        model = LiteLLMModel(
            model="claude-3-5-haiku-20241022",
            api_key="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"
        )
        super().__init__(model=model, *args, **kwargs)
        self.memory_file = memory_file
        self.system_prompt = SUMMARY_AGENT_PROMPT

    @tool
    def summarize_conversation(self, conversation: str) -> str:
        """
        Summarize a conversation, focusing on struggles, topics, exercises, and learning outcomes. Update the memory file accordingly.
        """
        # TODO: Use LLM to generate a summary from the conversation string
        summary = f"[Summary of conversation: {conversation[:50]}...]"  # Placeholder
        self._update_memory_file(summary)
        return summary

    @tool
    def summarize_memory(self, memory: str) -> str:
        """
        Summarize the memory file, focusing on struggles, topics, exercises, and learning outcomes.
        """
        # TODO: Use LLM to generate a summary from the memory string
    @tool
    def read_memory(self) -> str:
        """
        Read the current memory file contents.
        """
        if not os.path.exists(self.memory_file):
            return ""
        with open(self.memory_file, "r") as f:
            return f.read()

    @tool
    def write_memory(self, content: str) -> str:
        """
        Overwrite the memory file with new content.
        """
        with open(self.memory_file, "w") as f:
            f.write(content)
        return "Memory file updated."

    def _update_memory_file(self, new_summary: str):
        """
        Internal method to update the memory file, keeping it concise.
        """
        old_content = self.read_memory()
        # TODO: Implement logic to merge new_summary with old_content, trim if too long
        updated_content = (old_content + "\n" + new_summary).strip()
        # Example: keep only last 2000 characters
        if len(updated_content) > 2000:
            updated_content = updated_content[-2000:]
        self.write_memory(updated_content)

def process_new_conversation(agent: SummaryAgent, conversation_path: str):
    """
    Working loop for summarizing a new conversation and updating the memory file.
    1. Read the latest conversation
    2. Summarize it
    3. Read the memory file
    4. If memory file > 2000 chars, prompt agent to summarize/condense it
    5. Otherwise, leave unchanged
    6. Append the summary of last interaction to the file, prepending the date
    """
    # 1. Read the latest conversation
    with open(conversation_path, 'r') as f:
        conversation = f.read()

    # 2. Summarize it
    summary = agent.summarize_conversation(conversation)
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    dated_summary = f"[{date_str}]\n{summary}"

    # 3. Read the memory file
    memory = agent.read_memory()

    # 4. If memory file > 2000 chars, condense it
    if len(memory) > 2000:
        print("Memory file too long, condensing...")
        # Prompt the agent to summarize/condense the memory
        condensed = agent.summarize_memory(memory)
        memory = f"[Condensed on {date_str}] {condensed}"

    # 6. Append the summary of last interaction to the file
    updated_memory = (memory + "\n" + dated_summary).strip() if memory else dated_summary
    agent.write_memory(updated_memory)
    print("Memory file updated.")

# Example usage
if __name__ == "__main__":
    agent = SummaryAgent()
    # Replace 'latest_conversation.txt' with your actual conversation file path
    process_new_conversation(agent, 'latest_conversation.txt') 