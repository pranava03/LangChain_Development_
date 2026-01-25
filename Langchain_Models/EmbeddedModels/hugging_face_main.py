from langchain_huggingface import HuggingFaceEmbeddings
from config import settings

embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2", huggingfacehub_api_token = settings.huggingfacehub_access_token)
text       = "Delhi is the capital of India."
result     = embeddings.embed_query(text)
documents  = ["Mumbai is the financial capital of India.", "Python is a programming language."]
result1    = embeddings.embed_documents(documents)
print(str(result1))
print(str(result))