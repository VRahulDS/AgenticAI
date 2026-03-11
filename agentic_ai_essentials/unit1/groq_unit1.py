from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="qwen/qwen3-32b"
)
response = llm.invoke("What is agentic AI?")
print(response)