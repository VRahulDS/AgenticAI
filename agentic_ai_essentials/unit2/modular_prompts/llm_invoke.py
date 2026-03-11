from typing import Optional, Dict, Any
from llms import get_llm
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from prompt_builder import build_prompt_from_config
from utils import save_text_to_file
from essentials_paths import OUTPUTS_DIR



def invoke_llm(
    prompt: str, model: str = "llama-3.1-8b-instant", temperature: float = 0.0
) -> Optional[str]:
    """Calls the LLM with a prompt and returns the response.

    Args:
        prompt: The prompt to send to the LLM.
        model: The LLM model to use.
        temperature: Sampling temperature.

    Returns:
        The LLM's response content, or None if an error occurs.
    """
    try:
        llm = get_llm(model)
        message = HumanMessage(content=prompt)
        response = llm.invoke([message])
        return response.content
    except Exception as e:
        print(f"Error calling LLM: {e}")
        return None
    


def run_prompt_example(
    all_prompts_config: Dict[str, Any],
    prompt_config_key: str,
    publication_content: str,
    model_name: str,
    app_config: Dict[str, Any],
) -> None:
    """Builds a prompt, runs it with the LLM, and saves the response.

    Args:
        all_prompts_config: Dictionary of all available prompt configurations.
        prompt_config_key: Key identifying the specific prompt config to use.
        publication_content: Content to summarize or process.
        model_name: Name of the LLM to use.
        app_config: Application-level config (e.g. reasoning strategies).
    """
    # Build the prompt
    if prompt_config_key not in all_prompts_config:
        print(f"Config key '{prompt_config_key}' not found in configuration")
        return

    prompt_config = all_prompts_config[prompt_config_key]

    # Pass app_config to build_prompt_from_config
    prompt = build_prompt_from_config(prompt_config, publication_content, app_config)
    output_prompt_path = OUTPUTS_DIR / f"{prompt_config_key}_prompt.md"
    save_text_to_file(
        prompt,
        output_prompt_path,
        header=f"Prompt Generated From Config: {prompt_config_key}",
    )

    # Get LLM response
    llm_response = invoke_llm(prompt, model=model_name)
    output_llm_path = OUTPUTS_DIR / f"{prompt_config_key}_llm_response.md"
    if llm_response:
        save_text_to_file(
            llm_response,
            output_llm_path,
            header=f"LLM Response for Prompt: {prompt_config_key}",
        )
    else:
        print("✗ LLM response was empty or failed.")