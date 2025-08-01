# LangChain Integration with Python Automation Framework

This project demonstrates how to integrate **LangChain** into a Python-based automation test framework using **OpenRouter** as the LLM backend. The goal is to empower your framework with AI-based decision-making and test healing when failures occur.

When a test fails—such as due to a broken locator—the framework captures the error and passes it to a LangChain agent, which analyzes the failure and suggests a possible fix. This enhances your test framework with intelligent, context-aware debugging support.


##  Requirements

- Python 3.9+
- Existing Python automation framework (custom, Behave, or Pytest-based)
- Browser setup (e.g., Chrome + ChromeDriver)
- OpenRouter account with a valid API key

##  Dependencies

Required libraries include:

- `langchain`
- `openai`
- `langchain-community`

##  OpenRouter Setup

To use LangChain with OpenRouter:

1. Go to [https://openrouter.ai](https://openrouter.ai)
2. Create an account or log in
3. Generate your API key at [https://openrouter.ai/keys](https://openrouter.ai/keys)
4. Use this key securely within your environment or configuration file

## Project Highlights

- AI-powered test healing triggered on failure
- Integration of LangChain agent using OpenRouter API
- Agent consumes error messages and test context
- Smart suggestions for debugging locator and logic errors
- Easily extensible for other automation scenarios

##  Execution

Once setup is complete:

1. Run your automation test suite normally.
2. If a failure is encountered, the LangChain agent will automatically be triggered.
3. The agent analyzes the error message and responds with a healing suggestion in your test output logs.

This makes the debugging process more intuitive and dramatically reduces manual effort in diagnosing test failures.


## Repository Contents

- `langchain_openrouter_agent.py`: Initializes and configures the LangChain agent
- `healing_agent.py`: Passes error messages and context to the agent
- `login_page.py` or other test files: Sample tests that demonstrate failure handling
- `README.md`: Project documentation


## Future Improvements

- Add automatic retries based on LLM suggestions
- Log healing recommendations in a dashboard or structured report
- Support for multiple LLM models (Meta, Cohere, Mistral, etc.)
- Integrate healing logic into a self-repairing test flow

