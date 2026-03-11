from essentials_paths import PROMPT_CONFIG_FPATH, APP_CONFIG_FPATH
from utils import load_env, load_publication, load_yaml_config
from llm_invoke import run_prompt_example
from pathlib import Path


def main(prompt_config_key: str)->None:
    try:
        print("loading environmental variables")
        load_env()
    except:
        print("unable to load environmetal file")

    try:
        print("loading publication data")
        publication_content = load_publication()
    except:
        print("unable to load the publication data")

    try:
        print("loading prompt configuration file")
        prompt_config = load_yaml_config(PROMPT_CONFIG_FPATH)
    except:
        print("unable to load the prompt configuration file")

    try:
        print("loading configuration file")
        config = load_yaml_config(APP_CONFIG_FPATH)
        model_name = config.get("llm")
    except:
        print("unable to load the configuration file")

    if prompt_config_key not in prompt_config:
        print(f"Error: Prompt config key '{prompt_config_key}' not found.")
        return

    print(f"\nRunning prompt example: {prompt_config_key}")
    run_prompt_example(
        all_prompts_config=prompt_config,
        prompt_config_key=prompt_config_key,
        publication_content=publication_content,
        model_name=model_name,
        app_config=config,
    )

    print(f"\n{'-'*80}")
    print("TASK COMPLETE!")
    print("=" * 80)


if __name__ == "__main__":

    prompt_cfg_key = "summarization_prompt_cfg6"
    main(prompt_config_key=prompt_cfg_key)