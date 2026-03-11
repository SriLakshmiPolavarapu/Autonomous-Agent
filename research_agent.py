import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# tool calling
def search_web(query: str) -> dict:
    """Search the web for the information on a topic."""
    return{}

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    tools=[search_web],
    system_instruction="You are a research agent. When asked about current events or recent information, ALWAYS use the search_web tool. Never answer from memory."
)

response = model.generate_content("Search for the latest trends in edge AI")


print(response.candidates[0].content.parts)