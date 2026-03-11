from src.retrieval.retrieve_doc import retrieve_doc
from src.logging.logger import setup_logger
from utils import load_yaml_config
from rag_paths import APP_CONFIG_FPATH, PROMPT_CONFIG_FPATH
from src.response.response import respond_to_query

import logging
logger = logging.getLogger(__name__)

setup_logger()
app_config = load_yaml_config(APP_CONFIG_FPATH)
prompt_config = load_yaml_config(PROMPT_CONFIG_FPATH)

rag_assistant_prompt = prompt_config["rag_assistant_prompt"]

vectordb_params = app_config["vectordb"]
llm = app_config["llm"]

exit_app = False
while not exit_app:
    query = input(
        "Enter a question, 'config' to change the parameters, or 'exit' to quit: "
    )
    if query == "exit":
        exit_app = True
        exit()

    elif query == "config":
        threshold = float(input("Enter the retrieval threshold: "))
        n_results = int(input("Enter the Top K value: "))
        vectordb_params = {
            "threshold": threshold,
            "n_results": n_results,
        }
        continue

    response = respond_to_query(
        prompt_config=rag_assistant_prompt,
        query=query,
        llm=llm,
        **vectordb_params,
    )
    logging.info("-" * 100)
    logging.info("LLM response:")
    logging.info(response + "\n\n")