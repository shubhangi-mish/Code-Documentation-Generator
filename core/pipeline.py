from agents.func_extractor import FunctionExtractor
from agents.docstring_gen import DocstringGenerator
from agents.code_explain import CodeExplainer
from agents.refactoring_agent import RefactoringAgent

class DocumentationPipeline:
    def __init__(self):
        self.extractor = FunctionExtractor()
        self.docstring_gen = DocstringGenerator()
        self.explainer = CodeExplainer()
        self.refactor = RefactoringAgent()

    def generate_documentation(self, code):
        """Runs all agents and returns structured documentation."""
        functions = self.extractor.extract_functions(code)
        documentation = {}

        if not functions:
            print("⚠️ No functions extracted! Check FunctionExtractor.")  # Debugging info

        for function in functions:
            print(f"Processing function: {function.name}")  # Debugging info
            documentation[function.name] = {
                "docstring": self.docstring_gen.generate_docstring(function.code),
                "explanation": self.explainer.explain_code(function.code),
                "refactoring": self.refactor.suggest_improvements(function.code),
            }

        return documentation