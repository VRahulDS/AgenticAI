from rag_paths import DATA_DIR, LOG_DIR
import logging
logger = logging.getLogger(__name__)

def read_pubs_content(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if len(content) > 0:
        logger.info(f"read the file: {file_path}")

    else:
        logger.info(f"unable to read the file: {file_path}")

    return content
