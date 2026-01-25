from langchain_openai import ChatOpenAI
from config import settings

model  = ChatOpenAI(model = "gpt-4o", api_key = settings.openai_api_key, temperature = 1.5, max_completion_tokens = 1024)
result = model.invoke("Write a 5 line poem about cricket")
print(result.content)