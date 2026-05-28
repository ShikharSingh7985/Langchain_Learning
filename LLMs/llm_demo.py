from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv

llm=OpenAI(model="gpt")

result =llm.invoke("What is Capital of India ")

print(result)
