from langchain_anthropic import ChatAnthropic
from config import settings

model  = ChatAnthropic(model = "claude-3-5-sonnet", api_key = settings.anthropic_api_key, temperature = 1.5, max_completion_tokens = 1024)
result = model.invoke("Write a 5 line poem about cricket")
print(result.content)