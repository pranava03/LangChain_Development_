from langchain_google_genai import ChatGoogleGenerativeAI
from config import settings

model  = ChatGoogleGenerativeAI(model = "gemini-1.5-pro", api_key = settings.google_api_key, temperature = 0.7, max_output_tokens = 1024)
result = model.invoke("Explain the theory of relativity in simple terms.")
print(result.content)