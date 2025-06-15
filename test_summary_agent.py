
import datetime
from agents.memory_agent import update_memory

latest_conversation = """
Agent: Hi Alex! Today we're going to practice integrating x^2 from 0 to 1. Are you ready?
Student: I think so, but I'm not sure where to start.
Agent: No problem! What's the first thing you remember about integrating polynomials?
Student: I think I need to use the power rule, but I always get confused about the exponent.
Agent: Great! The power rule says to add one to the exponent and divide by the new exponent. What would that look like for x^2?
Student: So it would be x^3/3?
Agent: Exactly! Now, since this is a definite integral from 0 to 1, what do you do next?
Student: Plug in the limits?
Agent: Yes! Can you try plugging in the upper and lower limits and subtracting?
Student: Okay, so (1^3/3) - (0^3/3) = 1/3 - 0 = 1/3.
Agent: Perfect! You did it step by step. How do you feel about this process now?
Student: I think I get it better now, but I still worry about more complicated polynomials.
Agent: That's normal! We can practice more examples together. Would you like to try another one?
Student: Yes, please! 
"""

def test_summary_agent_updates_memory():
    # Setup: copy pseudo files to temp dir
    memory_file = "student_memory.md"
    conversation_file = "latest_conversation.txt"

    # Run the summarization workflow
    update_memory(latest_conversation)

    # Check that the memory file was updated
    with open(memory_file, "r") as f:
        updated = f.read()
    print(updated)
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    assert today in updated, "Today's date should be in the updated memory file."
    assert "integrating x^2" in updated.lower() or "integrate x^2" in updated.lower(), "Summary of the new conversation should be present."

if __name__ == "__main__":
    import tempfile
    test_summary_agent_updates_memory()
    print("Test passed.") 