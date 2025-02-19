from crewai.tools import tool
from models.gemini_integ import GeminiModel

class CodeExplainer:
    def __init__(self):
        self.deepseek = GeminiModel()

    @tool
    def explain_code(self, function_code: str) -> str:
        """Provides a human-readable explanation of the given function."""
        prompt = f"Explain this function in simple terms:\n{function_code}"
        return self.deepseek.generate_text(prompt)
