from utils.langchain_openrouter_agent import get_langchain_agent


def analyze_and_heal_failure(error_message: str, context_data: dict = None):
    agent = get_langchain_agent()

    prompt = f"""
    We have an automation test failure. Here's the error message:
    ---
    {error_message}
    ---
    Can you suggest a possible healing approach? Assume it's related to web element identification or test logic.

    If you need, here's some context:
    {context_data if context_data else "No additional context"}
    """

    response = agent.run(prompt)
    return response
