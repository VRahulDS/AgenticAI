import chromadb
from rag_paths import DB_DIR



def initialize_DB(reset=False):

    client = chromadb.PersistentClient(path=DB_DIR)

    if reset:
        try:
            client.delete_collection("publications")
        except:
            pass

    collection = client.get_or_create_collection(
        name="publications"
    )

    return collection