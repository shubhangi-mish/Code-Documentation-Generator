import ast
import astor
from crewai.tools import tool  # ✅ Correct way to define a CrewAI tool

class FunctionExtractor:
    """Extracts function definitions from Python code."""

    @tool  # ✅ CrewAI recognizes this as a valid tool
    def extract_functions(code: str):
        """Extracts function definitions from Python code."""
        tree = ast.parse(code)
        functions = []

        for node in ast.walk(tree):  # Walk through all nodes
            if isinstance(node, ast.FunctionDef):  # Extract any function
                func_name = node.name  
                try:
                    func_code = ast.unparse(node)  # Extract full function code
                except AttributeError:  # If Python <3.9, use astor
                    func_code = astor.to_source(node)
                functions.append({"name": func_name, "code": func_code})

        print(functions)  # Debugging output
        return functions
