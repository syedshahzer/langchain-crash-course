from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from os import getenv
# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
# model = ChatOpenAI(model="gpt-4o")

# model = ChatOpenRouter(model="meta-llama/llama-3.3-8b-instruct:free")
model = ChatOpenAI(
    # api_key=getenv("OPENROUTER_API_KEY"),
  openai_api_key=getenv("OPENROUTER_API_KEY"),
  openai_api_base="https://openrouter.ai/api/v1",
#   model_name="meta-llama/llama-3.3-8b-instruct:free",
model_name="nousresearch/deephermes-3-mistral-24b-preview:free"

)

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
