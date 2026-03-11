import logging
from src.ingestion.embed_document import model
from src.db_setup.initialize_db import initialize_DB
logger = logging.getLogger(__name__)

collection = initialize_DB()

def retrieve_doc(query, n_results=6, threshold=0.5):
    logging.info(f"Retrieving relevant documents for query: {query}")
    relevant_results = {
        "ids": [],
        "documents": [],
        "distances": [],
    }
    logging.info("Embedding query...")

    query_embedding = model.embed_query(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "distances"],
    )

    logging.info("Filtering results...")
    keep_item = [True] * len(results["ids"][0])
    print(max(results["distances"]), min(results["distances"]))
    for i, distance in enumerate(results["distances"][0]):
        if distance < threshold:
            keep_item[i] = True

    for i, keep in enumerate(keep_item):
        if keep:
            relevant_results["ids"].append(results["ids"][0][i])
            relevant_results["documents"].append(results["documents"][0][i])
            relevant_results["distances"].append(results["distances"][0][i])

    return relevant_results["documents"]



