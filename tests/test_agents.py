import unittest
from agents.func_extractor import FunctionExtractor
from agents.docstring_gen import DocstringGenerator
from agents.code_explain import CodeExplainer
from agents.refactoring_agent import RefactoringAgent

class TestAgents(unittest.TestCase):
    def setUp(self):
        self.extractor = FunctionExtractor()
        self.docstring_gen = DocstringGenerator()
        self.explainer = CodeExplainer()
        self.refactor = RefactoringAgent()

        self.sample_code = """
        def add(a, b):
            return a + b
        """

    def test_function_extractor(self):
        functions = self.extractor.extract_functions(self.sample_code)
        self.assertEqual(len(functions), 1)
        self.assertEqual(functions[0].name, "add")

    def test_docstring_generator(self):
        docstring = self.docstring_gen.generate_docstring(self.sample_code)
        self.assertIsInstance(docstring, str)
        self.assertTrue(len(docstring) > 0)

    def test_code_explainer(self):
        explanation = self.explainer.explain_code(self.sample_code)
        self.assertIsInstance(explanation, str)
        self.assertTrue("adds two numbers" in explanation.lower())

    def test_refactoring_agent(self):
        suggestions = self.refactor.suggest_improvements(self.sample_code)
        self.assertIsInstance(suggestions, str)
        self.assertTrue("improve" in suggestions.lower())

if __name__ == "__main__":
    unittest.main()
