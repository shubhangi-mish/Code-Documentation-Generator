import streamlit as st
from models.crewai_setup import DocumentationCrew

# Streamlit UI Header
st.set_page_config(page_title="AI Code Documentor", layout="wide")
st.title("📝 AI-Powered Code Documentation Generator")

# Text area for user input
code = st.text_area("Paste your Python code below:", height=250)

# Button to generate documentation
if st.button("Generate Documentation"):
    if code.strip():
        st.subheader("📜 Generated Documentation")
        
        # Run the Crew Pipeline
        pipeline = DocumentationCrew()
        docs = pipeline.generate_documentation(code)

        # Display results
        for func_name, details in docs.items():
            st.write(f"### 🔹 Function: `{func_name}`")
            st.write(f"**📌 Docstring:**\n```python\n{details['docstring']}\n```")
            st.write(f"**📖 Explanation:**\n{details['explanation']}")
            st.write(f"**🛠️ Refactoring Suggestions:**\n{details['refactoring']}")
            st.markdown("---")
    else:
        st.warning("⚠️ Please enter some Python code before generating documentation.")
