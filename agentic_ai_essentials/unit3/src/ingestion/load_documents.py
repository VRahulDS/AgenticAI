

from src.ingestion.file_reader import read_pubs_content
from src.ingestion.chunk_document import chunk_document
from src.db_setup.initialize_db import initialize_DB
from src.ingestion.embed_document import embed_document

import logging
logger = logging.getLogger(__name__)

collection = initialize_DB(True)

def load_documents(dir_path):

    try:

        all_files = dir_path.glob("*.txt")

        next_id = collection.count()

        for file in all_files:
            content = read_pubs_content(file)
            chunks = chunk_document(content)
            embeds = embed_document(chunks)

            ids = list(range(next_id, next_id + len(chunks)))
            ids = [f"document_{id}" for id in ids]

            collection.add(
                embeddings=embeds,
                ids=ids,
                documents=chunks
            )

            next_id += len(chunks)

            logger.info(f"added the chunks for file: {file}")

    except:
        logger.info("failed ingesting thew documnets")



