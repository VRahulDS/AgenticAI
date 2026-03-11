from src.logging.logger import setup_logger
from src.ingestion.load_documents import load_documents
from rag_paths import DATA_DIR

logger = setup_logger()

logger.info("Application started")

load_documents(DATA_DIR)