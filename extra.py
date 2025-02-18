from core.pipeline import DocumentationPipeline

pipeline = DocumentationPipeline()
code = "def hello():\n    return 'Hello, world!'"
docs = pipeline.generate_documentation(code)
print(docs)