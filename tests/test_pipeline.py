import unittest
from core.pipeline import DocumentationPipeline

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.pipeline = DocumentationPipeline()
        self.sample_code = """
        def multiply(a, b):
            return a * b
        """

    def test_pipeline(self):
        docs = self.pipeline.generate_documentation(self.sample_code)
        self.assertIn("multiply", docs)
        self.assertTrue("docstring" in docs["multiply"])
        self.assertTrue("explanation" in docs["multiply"])
        self.assertTrue("refactoring" in docs["multiply"])

if __name__ == "__main__":
    unittest.main()
