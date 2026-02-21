from langchain_community.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults

search_tool = DuckDuckGoSearchRun()
# search_tool = DuckDuckGoSearchResults()

results = search_tool.invoke("top news in india today") # This is also a runnbale!! 

print(results)