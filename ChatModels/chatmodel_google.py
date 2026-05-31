from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

models= ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

result=models.invoke("what is capital of new delhi")

# Access the text element in the first block
print(print(result.content[0]["text"]))
