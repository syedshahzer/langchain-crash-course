from os import getenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage

# Setup environment variables and messages
load_dotenv()

messages = [
    SystemMessage(content="Provide latest and precise information about the topic. Be concise."),
    HumanMessage(content="most important organ in human body."),
]


# ---- LangChain OpenAI Chat Model Example ----

# Create a ChatOpenAI model
model = ChatOpenAI(
    openai_api_key=getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model_name="qwen/qwen3-235b-a22b:free"
)

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from Qwen 3: {result.content}")


# ---- Anthropic Chat Model Example ----

# Create a Anthropic model
# Anthropic models: https://docs.anthropic.com/en/docs/models-overview
model = ChatOpenAI(
    openai_api_key=getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model_name="meta-llama/llama-4-maverick:free"
)

result = model.invoke(messages)
print(f"Answer from LLama 4 maverick: {result.content}")


# ---- Google Chat Model Example ----

# https://console.cloud.google.com/gen-app-builder/engines
# https://ai.google.dev/gemini-api/docs/models/gemini
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

result = model.invoke(messages)
print(f"Answer from Google: {result.content}")

# # ---- Ollama Chat Model Example ----
# # https://ollama.com/models
# model = OllamaChat(model="gemma3")
# result = model.invoke(messages)
# print(f"Answer from Ollama: {result.content}")

# model = OllamaChat(model="deepseek-r1")
# result = model.invoke(messages)
# print(f"Answer from Deepseek R1: {result.content}")
