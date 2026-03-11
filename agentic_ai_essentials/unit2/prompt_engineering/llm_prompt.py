from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv
import prompt_1
import prompt_2
import prompt_3
import prompt_4
import prompt_5

load_dotenv()

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)

# Basic question

messages = prompt_5.get_prompt()[:2000]


response = llm.invoke(messages)
print(response.content)
