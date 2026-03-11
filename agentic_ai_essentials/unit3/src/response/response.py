from src.retrieval.retrieve_doc import retrieve_doc
from src.prompt_builder import build_prompt_from_config
from rag_paths import ENV_FPATH
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import logging
logger = logging.getLogger(__name__)

load_dotenv(ENV_FPATH)



def respond_to_query(
    prompt_config: dict,
    query: str,
    llm: str,
    n_results: int = 2,
    threshold: float = 0.3,
) -> str:
    """
    Respond to a query using the ChromaDB database.
    """

    relevant_documents = retrieve_doc(
        query, n_results=n_results, threshold=threshold
    )

    # logging.info("-" * 100)
    # logging.info("Relevant documents: \n")
    # # for doc in relevant_documents:
    # #     # logging.info(doc)
    # #     logging.info("-" * 100)
    # logging.info("")

    logging.info("User's question:")
    logging.info(query)
    logging.info("")
    logging.info("-" * 100)
    logging.info("")
    input_data = (
        f"Relevant documents:\n\n{relevant_documents}\n\nUser's question:\n\n{query}"
    )

    rag_assistant_prompt = build_prompt_from_config(
        prompt_config, input_data=input_data
    )

    logging.info(f"RAG assistant prompt: {rag_assistant_prompt}")
    logging.info("")

    llm = ChatGroq(model=llm)

    response = llm.invoke(rag_assistant_prompt)
    return response.content