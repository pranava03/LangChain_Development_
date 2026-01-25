from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from config import settings
import os

os.environ["HF_HOME"] = "D:/Local_Folders/miscellaneous_playgorund/Latest/Latest_3/HuggingFace_Cache"

llm    = HuggingFacePipeline.from_model_id(model_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0', task = 'text-generation', huggingfacehub_api_token = settings.huggingfacehub_access_token, pipeline_kwargs = dict(temperature = 0.8, max_new_tokens = 256))
model  = ChatHuggingFace(llm = llm)
result = model.invoke("What is the capital of France?")
print(result.content)