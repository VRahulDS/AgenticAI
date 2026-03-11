import logging
import torch
from langchain_huggingface import HuggingFaceEmbeddings

logger = logging.getLogger(__name__)

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps" if torch.backends.mps.is_available()
    else "cpu"
)

model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": device},
)


def embed_document(documents):

    if len(documents) == 0:
        logger.info("Chunk file is empty")
        return []

    try:
        embeddings = model.embed_documents(documents)
        logger.info(f"Created embeddings for {len(documents)} documents")
        return embeddings

    except Exception as e:
        logger.error(f"Embedding failed: {e}")
        return []