from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

models= ChatGoogleGenerativeAI(model="gemini-2.5-flash")

result=models.invoke("What is the capital of india?")

# Access the text element in the first block
print(result.content)
