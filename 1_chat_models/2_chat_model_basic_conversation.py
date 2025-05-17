from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from os import getenv
# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(
    openai_api_key=getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model_name="deepseek/deepseek-chat-v3-0324:free"
)

# SystemMessage:
#   Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
# HumanMessagse:
#   Message from a human to the AI model.
# messages = [
#     SystemMessage(content="Solve the following math problems"),
#     HumanMessage(content="What is 81 divided by 9?"),
# ]

# # Invoke the model with messages
# result = model.invoke(messages)
# print(f"Answer from AI: {result.content}")


# AIMessage:
#   Message from an AI.
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?"),
    AIMessage(content="10 times 5 is 50."),
    HumanMessage(content="What was my second question?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")
