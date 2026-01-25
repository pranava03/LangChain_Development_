from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from config import settings

llm    = HuggingFaceEndpoint(repo_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0', task = 'text-generation', huggingfacehub_api_token = settings.huggingfacehub_access_token)#, model_kwargs = {'temperature':0.7, 'max_new_tokens':256})
llm    = HuggingFaceEndpoint(repo_id = 'HuggingFaceH4/zephyr-7b-beta', task = 'text-generation', huggingfacehub_api_token = settings.huggingfacehub_access_token)
model  = ChatHuggingFace(llm = llm)
result = model.invoke("What is the capital of France?")
print(result.content)