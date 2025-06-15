from smolagents import ToolCallingAgent, tool, LiteLLMModel
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

Please ALWAYS use LATEX to write math equations.

"""

class ExerciseTrainerAgent(ToolCallingAgent):
    """
    Agent dedicated to guiding a student through a specific exercise step by step.
    Provides interactive guidance, hints, and solutions while encouraging student learning.
    
    Attributes:
        exercise (Exercise): The current exercise being worked on
        memory_summary (str): Summary of previous interactions with the student
    """
    def __init__(self, memory_summary: str = "", *args, **kwargs):
        """
        Initialize the ExerciseTrainerAgent with a specific exercise and optional memory context.
        
        Args:
            problem (str): The problem to work on
            solution (str): The solution to the problem
            memory_summary (str, optional): Summary of previous interactions. Defaults to "".
            *args: Additional positional arguments for MultiStepAgent
            **kwargs: Additional keyword arguments for MultiStepAgent
            
        Raises:
            ValueError: If the specified exercise is not found in the database
        """

        print(f"Initializing ExerciseTrainerAgent with memory_summary: {memory_summary}")

        model = LiteLLMModel(
            model="claude-opus-4-20250514", 
            api_key="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"
        )

        super().__init__(
            name="ExerciseTrainerAgent",
            description="Agent used to help the student solve the exercise",
            model=model,
            *args,
            **kwargs,
            tools=[]
        )
        self.memory_summary = memory_summary

    def initialize_system_prompt(self) -> str:
        return EXERCISE_TRAINER_PROMPT


