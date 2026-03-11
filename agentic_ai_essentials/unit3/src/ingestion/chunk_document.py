from langchain_text_splitters import RecursiveCharacterTextSplitter
import logging
logger = logging.getLogger(__name__)

def chunk_document(file_content, chunk_size=6000, overlap_size=50):
    if len(file_content) > 0:
        try:
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=overlap_size
            )

            chunks = splitter.split_text(file_content)
            logger.info("chunks are created")
        except:
            logger.info("unable to create the chunks")
    
    else:
        logger.info("chunk failed as the content is empty")


    return chunks