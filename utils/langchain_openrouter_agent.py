import os
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory


def get_langchain_agent():
    llm = ChatOpenAI(
        temperature=0.2,
        model="openai/gpt-3.5-turbo",  # You can also use `openrouter/meta-llama`, etc.
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key="OPENROUTER_API_KEY"
    )

    tools = []  # You can define tools for debugging, rerunning, etc.

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True
    )
    return agent
