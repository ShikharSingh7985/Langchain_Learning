"""
Overall Intuition:
- This code uses Google Gemini embeddings through LangChain.
- It loads the API key from the .env file.
- Then it creates an embedding model with output dimension 10.
- After that, it converts the sentence "Delhi is the Capital of india" into a numerical vector.
- Finally, it prints that embedding vector as a string.
"""

from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Imports the Google Gemini embedding class from LangChain

from dotenv import load_dotenv  # Imports load_dotenv to load environment variables from the .env file

load_dotenv()  # Loads environment variables like GOOGLE_API_KEY from the .env file

embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-2",dimension=10)  # Creates a Gemini embedding model object with embedding vector size 10

result =embedding.embed_query("Delhi is the Capital of india ")  # Converts the given text query into an embedding vector

print(str(result))  # Converts the embedding vector into a string and prints it