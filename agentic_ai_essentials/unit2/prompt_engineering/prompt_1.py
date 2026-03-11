def get_prompt():

    with open(r"agentic_ai_essentials\unit2\prompt_engineering\published_data.txt", "r") as f:
        publication = f.read()

    messages = f"""
        your task is as follows:
        write a summary of an article or publication given to you.

        Here is the conetent you need to work with:

        <<<BEGIN CONTENT>>>
        {publication}
        <<<END CONTENT>>>

        Now perform the task as instructed above
    """
    return messages


