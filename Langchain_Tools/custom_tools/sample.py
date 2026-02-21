# Creating the tool with the @tool decorator...

from langchain_core.tools import tool

# Step 1, 2, 3 - create a function & add type hints & add tool decorator.

@tool
def multiply(a: int, b: int) -> int:
    """ Multiply two numbers """
    return a * b

result = multiply.invoke({"a" : 3, "b" : 3})
print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.args_schema.model_json_schema())