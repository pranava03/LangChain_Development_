from langchain_openai import OpenAI
from config import settings

llm    = OpenAI(model = "gpt-5.5-turbo", api_key = settings.openai_api_key)
result = llm.invoke("What is the capital of India?")
print(result)