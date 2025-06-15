from smolagents import MultiStepAgent, tool, LiteLLMModel
from dataclasses import dataclass
from typing import Dict, Optional

EXERCISE_TRAINER_PROMPT = """
You are a dedicated exercise trainer for STEM students. Your job is to guide the student through a specific exercise, step by step, without revealing the answer unless absolutely necessary.

Guidelines:
- Start by restating the exercise and asking the student what they think the first step is.
- Encourage the student to think aloud and explain their reasoning.
- If the student is stuck, offer hints or break the problem into smaller parts.
- Never give away the answer immediately. Only provide the answer if the student insists or is unable to proceed after multiple hints.
- Be patient, supportive, and adapt your guidance to the student's level and previous struggles (if provided).
- At the end, summarize what the student learned and suggest similar exercises for further practice.
"""

@dataclass  
class Exercise:
    id: str
    problem: str
    hints: str
    solution: str

# In-memory exercise database (replace with actual database in production)
_exercise_db: Dict[str, Exercise] = {}

def get_exercise(exercise_id: str) -> Optional[Exercise]:
    """
    Retrieve an exercise from the database by its ID.
    
    Args:
        exercise_id (str): The ID of the exercise to retrieve
        
    Returns:
        Optional[Exercise]: The exercise if found, None otherwise
    """
    return _exercise_db.get(exercise_id)

def add_exercise(exercise: Exercise) -> None:
    """
    Add an exercise to the database.
    
    Args:
        exercise (Exercise): The exercise to add
    """
    _exercise_db[exercise.id] = exercise

@tool
def consult_hints(exercise_id: str) -> str:
    """
    Consult the tips for the given exercise.
    """
    exercise = get_exercise(exercise_id)
    if not exercise:
        return f"Exercise {exercise_id} not found."
    return f"Here are some hints for the exercise: {exercise.hints}"

def consult_solution(exercise_id: str) -> str:
    """
    Consult the solution for the given exercise.
    """
    exercise = get_exercise(exercise_id)
    if not exercise:
        return f"Exercise {exercise_id} not found."
    return f"Here is the solution for the exercise: {exercise.solution}"

class ExerciseTrainerAgent(MultiStepAgent):
    """
    Agent dedicated to guiding a student through a specific exercise step by step.
    """
    def __init__(self, exercise_id: str, memory_summary: str = "", *args, **kwargs):
        model = LiteLLMModel(
            model="claude-opus-4-20250514", 
            api_key="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"
        )
        
        tools = [
            consult_hints,
            consult_solution
        ]

        exercise = get_exercise(exercise_id)
        if not exercise:
            raise ValueError(f"Exercise {exercise_id} not found.")
        
        super().__init__(
            tools=tools,
            model=model,
            prompt_templates={"system": EXERCISE_TRAINER_PROMPT + f"\nExercise ID: {exercise_id}\nExercise: {exercise.problem}\nPrevious conversation: {memory_summary}\n"},
            *args,
            **kwargs
        )
        self.exercise = exercise
        self.memory_summary = memory_summary
