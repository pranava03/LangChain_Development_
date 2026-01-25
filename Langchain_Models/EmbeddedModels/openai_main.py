from langchain_openai import OpenAIEmbeddings
from config import settings

embeddings = OpenAIEmbeddings(api_key = settings.openai_api_key, model = "text-embedding-3-large", dimensions = 32)
result     = embeddings.embed_query("Delhi is the capital of India.")
documents  = ["Mumbai is the financial capital of India.", "Python is a programming language."]
result1    = embeddings.embed_documents(documents)
print(str(result))
print(str(result1))