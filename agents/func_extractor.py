import ast
import astor
from collections import namedtuple

FunctionInfo = namedtuple("FunctionInfo", ["name", "code"])

class FunctionExtractor:
    def extract_functions(self, code):
        """Parses Python code and extracts function definitions (including class methods)."""
        tree = ast.parse(code)
        functions = []

        for node in ast.walk(tree):  # Walk through all nodes
            if isinstance(node, ast.FunctionDef):  # Extract any function
                func_name = node.name  
                try:
                    func_code = ast.unparse(node)  # Extract full function code
                except AttributeError:  # If Python <3.9, use astor
                    import astor
                    func_code = astor.to_source(node)
                functions.append(FunctionInfo(name=func_name, code=func_code))

        print(functions)
        return functions
