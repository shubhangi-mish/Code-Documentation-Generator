from crewai.tools import tool
from models.gemini_integ import GeminiModel

class DocstringGenerator:
    def __init__(self):
        self.deepseek = GeminiModel()

    @tool
    def generate_docstring(self, function_code: str) -> str:
        """Generates a meaningful docstring for a given function."""
        prompt = f"Generate a docstring for this function:\n{function_code}"
        return self.deepseek.generate_text(prompt)
