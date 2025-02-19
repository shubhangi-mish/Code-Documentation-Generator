from crewai.tools import tool
from models.gemini_integ import GeminiModel

class RefactoringAgent:
    def __init__(self):
        self.deepseek = GeminiModel()

    @tool
    def suggest_improvements(self, function_code: str) -> str:
        """Suggests improvements for the given function."""
        prompt = f"Suggest improvements for this function:\n{function_code}"
        return self.deepseek.generate_text(prompt)
