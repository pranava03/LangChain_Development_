from langchain_openai import OpenAIEmbeddings
from config import settings
from sklearn.metrics.pairwise import cosine_similarity

emmbedding          = OpenAIEmbeddings(api_key=settings.openai_api_key, model = 'text-embedding-3-large', dimensions = 300)
documents           = ["Virat Kohli is a great cricketer.", "MS Dhoni is a good captain.", "Rohit Sharma is an excellent batsman.", "Sachin Tendulkar is a legendary player.", "Adam Gilchrist is a fantastic wicketkeeper."]
query               = "Tell me about virat kohli."
document_embeddings = emmbedding.embed_documents(documents)
query_embedding     = emmbedding.embed_query(query)
scores              = cosine_similarity([query_embedding], document_embeddings)[0]
index, score        = sorted(list(enumerate(scores)), key = lambda x: x[1])[-1]
print(query)
print(documents[index])
print(f"Similarity Score: {score}")