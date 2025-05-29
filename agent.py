from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory
from langchain_huggingface import HuggingFaceEndpoint
from recommender import recommend_cards

import os

 
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "add your token here"

 
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    temperature=0.7,
    max_new_tokens=512,
)

 
tools = [
    Tool(
        name="CreditCardRecommender",
        func=recommend_cards,
        description="Use this to recommend credit cards based on user's message"
    )
]

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True
)

def run_agent(user_message):
    return agent.run(user_message)
