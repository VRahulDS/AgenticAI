import os
from langchain_groq import ChatGroq
from essentials_paths import ENV_FPATH

from dotenv import load_dotenv

load_dotenv(ENV_FPATH)


available_models = [
    "llama-3.1-8b-instant",
    "llama-3.3-70b-versatile",
    "qwen/qwen3-32b"
]


def get_llm(model: str):
    if model not in available_models:
        raise ValueError(f"Invalid model. Available models: {available_models.keys()}")

    elif model in [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile",
        "qwen/qwen3-32b"
    ]:
        return ChatGroq(
            model_name=model,
            temperature=0.0,
            api_key=os.getenv("GROQ_API_KEY"),
        )