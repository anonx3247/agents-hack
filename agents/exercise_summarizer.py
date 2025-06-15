from smolagents import LiteLLMModel
from typing import List, Tuple

model = LiteLLMModel(
    model="claude-3-5-haiku-20241022",
    api_key="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"
)

def summarize_exercises(exercises: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """
    Generate concise titles for a list of exercises using Claude Haiku.
    
    Args:
        exercises (List[Tuple[str, str]]): List of (exercise_id, content) tuples
        
    Returns:
        List[Tuple[str, str]]: List of (exercise_id, title) tuples
    """
    # Format exercises for prompt
    formatted_exercises = "\n".join([f"[{id}]\n{content}" for id, content in exercises])
    
    prompt = f"""Given these exercises, generate a concise, descriptive title for each one.
The titles should be mathematical/scientific and capture the essence of the problem.
Return only the titles, one per line.

Exercises:
{formatted_exercises}"""

    messages = [
        {
            "role": "system",
            "content": "You are a mathematical exercise summarizer. Generate concise, descriptive titles for mathematical exercises."
        },
        {
            "role": "user", 
            "content": prompt
        }
    ]
    
    response = model.generate(messages).content
    
    # Parse response into list of titles
    titles = [line.strip() for line in response.split('\n') if line.strip()]
    
    # Return list of (id, title) tuples
    return list(zip([id for id, _ in exercises], titles))

