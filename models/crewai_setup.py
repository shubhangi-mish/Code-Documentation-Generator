from crewai import Crew
from agents.func_extractor import FunctionExtractor
from agents.docstring_gen import DocstringGenerator
from agents.code_explain import CodeExplainer
from agents.refactoring_agent import RefactoringAgent

class DocumentationCrew:
    def __init__(self):
        """Initialize Crew with all agents."""
        self.extractor = FunctionExtractor()
        self.docstring_gen = DocstringGenerator()
        self.explainer = CodeExplainer()
        self.refactor = RefactoringAgent()

        self.crew = Crew(
            name="Code Documentation Crew",
            description="A team of AI agents that analyze, explain, and improve Python code.",
            agents=[self.extractor, self.docstring_gen, self.explainer, self.refactor]
        )

    def generate_documentation(self, code):
        """Runs the crew to generate structured documentation."""
        functions = self.extractor.run(code)
        documentation = {}

        for function in functions:
            documentation[function["name"]] = {
                "docstring": self.docstring_gen.run(function),
                "explanation": self.explainer.run(function),
                "refactoring": self.refactor.run(function),
            }

        return documentation
