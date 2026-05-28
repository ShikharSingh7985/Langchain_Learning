"""
Overall Intuition:
- This code uses Google Gemini embedding model to convert text into numerical vectors.
- Each document sentence is converted into an embedding vector.
- The user query is also converted into an embedding vector.
- Then cosine similarity is used to compare the query with all documents.
- The document with the highest similarity score is selected as the best matching answer.
"""

from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Imports Gemini embedding class from LangChain
from dotenv import load_dotenv  # Imports function to load environment variables from .env file
from sklearn.metrics.pairwise import cosine_similarity  # Imports cosine similarity to compare vector similarity
import numpy as np  # Imports NumPy for numerical operations

load_dotenv()  # Loads API keys and environment variables from the .env file

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")  # Creates Gemini embedding model object

document = [  # Creates a list of text documents
"Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",  # Document about Virat Kohli
"MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",  # Document about MS Dhoni
"Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",  # Document about Sachin Tendulkar
"Rohit Sharma is known for his elegant batting and record-breaking double centuries.",  # Document about Rohit Sharma
"Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."  # Document about Jasprit Bumrah
]

query="Tell Me about Jasprit "  # Stores the user query that we want to search in the documents

doc_embeddings=embedding.embed_documents(document)  # Converts all documents into embedding vectors
query_embedding=embedding.embed_query(query)  # Converts the query into an embedding vector

scores=cosine_similarity([query_embedding],doc_embeddings)[0]  # Calculates similarity score between query and every document

index,score=sorted(list(enumerate(scores)) , key=lambda x:x[1])[-1]  # Sorts documents by similarity score and selects the highest scoring document

print(document[index])  # Prints the most similar document
print("similarity score is = "  , score)  # Prints the similarity score of the selected document