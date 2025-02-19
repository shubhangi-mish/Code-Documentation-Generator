from crewai import Crew, Agent, Task
from agents.func_extractor import FunctionExtractor
from agents.docstring_gen import DocstringGenerator
from agents.code_explain import CodeExplainer
from agents.refactoring_agent import RefactoringAgent

class DocumentationCrew:
    def __init__(self):
        self.function_extractor = Agent(
            role="Function Extractor",
            goal="Extract all functions from a Python script.",
            backstory="A software engineer specializing in Python code analysis.",
            verbose=True,
            allow_delegation=False,
            tools=[FunctionExtractor().extract_functions]  # ✅ Pass tool as a method
        )

        self.docstring_generator = Agent(
            role="Docstring Generator",
            goal="Generate docstrings for functions.",
            backstory="An AI that generates clear and concise docstrings.",
            verbose=True,
            allow_delegation=False,
            tools=[DocstringGenerator().generate_docstring]
        )

        self.code_explainer = Agent(
            role="Code Explainer",
            goal="Provide simple explanations for functions.",
            backstory="An AI that simplifies complex code explanations.",
            verbose=True,
            allow_delegation=False,
            tools=[CodeExplainer().explain_code] 
        )

        self.refactoring_agent = Agent(
            role="Refactoring Expert",
            goal="Provide suggestions to improve function code.",
            backstory="An AI that suggests optimizations and best practices.",
            verbose=True,
            allow_delegation=False,
            tools=[RefactoringAgent().suggest_improvements]
        )

        # Define Tasks
        extract_functions_task = Task(
            description="Extract functions from the given Python script.",
            agent=self.function_extractor
        )

        generate_docstring_task = Task(
            description="Generate docstrings for the extracted functions.",
            agent=self.docstring_generator
        )

        explain_code_task = Task(
            description="Explain the purpose of the extracted functions.",
            agent=self.code_explainer
        )

        refactor_code_task = Task(
            description="Refactor the extracted functions for better readability.",
            agent=self.refactoring_agent
        )

        # Define Crew
        self.crew = Crew(
            agents=[
                self.function_extractor,
                self.docstring_generator,
                self.code_explainer,
                self.refactoring_agent
            ],
            tasks=[
                extract_functions_task,
                generate_docstring_task,
                explain_code_task,
                refactor_code_task
            ],
            verbose=2
        )

    def generate_documentation(self, code):
        """Run the CrewAI workflow to generate documentation."""
        return self.crew.kickoff(inputs={"code": code})
