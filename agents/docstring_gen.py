from models.gemini_integ import GeminiModel

class DocstringGenerator:
    def __init__(self):
        self.deepseek = GeminiModel()

    def generate_docstring(self, function_code):
        """Generates a meaningful docstring for a function."""
        prompt = f"Generate a docstring for this function:\n{function_code}"
        msg=self.deepseek.generate_text(prompt)
        return msg
