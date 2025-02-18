import google.generativeai as genai
import os

class GeminiModel:
    def __init__(self):
        """Initialize Gemini model with API key."""
        self.api_key ="AIzaSyDNuLmLAX7Leq79d3LwcWCFce7OKfi-he4"
        genai.configure(api_key=self.api_key)

    def generate_text(self, prompt):
        """Calls Gemini API to generate text based on prompt."""
        model = genai.GenerativeModel("gemini-2.0-flash")  # Use the correct Gemini model
        response = model.generate_content(prompt)

        if response and response.candidates:
            return response.candidates[0].content
        else:
            raise Exception("Gemini API did not return a response.")
