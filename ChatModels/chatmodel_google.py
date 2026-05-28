from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

models= ChatGoogleGenerativeAI(model="gemini-3.5-flash")

result=models.invoke("What is the capital of india?")

print(result.content)