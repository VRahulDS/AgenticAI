def get_prompt():

    with open(r"agentic_ai_essentials\unit2\prompt_engineering\published_data.txt", "r") as f:
        publication = f.read()

    messages = f"""
        You are an AI communicator writing for a general public audience interested in technology and innovation.

        your task is as follows:
        write a summary of an article or publication given to you.

        Ensure your response follows these rules:
        - Keep the summary to a single paragraph of approximately 80 to 100 words
        - Avoid bullet points or section headers

        Here is the conetent you need to work with:

        <<<BEGIN CONTENT>>>
        {publication}
        <<<END CONTENT>>>

        Now perform the task as instructed above
    """
    return messages


