from models.gemini_integ import GeminiModel

class RefactoringAgent:
    def __init__(self):
        self.deepseek = GeminiModel()

    def suggest_improvements(self, function_code):
        """Suggests improvements to the function."""
        prompt = f"Suggest improvements for this function:\n{function_code}"
        return self.deepseek.generate_text(prompt)
