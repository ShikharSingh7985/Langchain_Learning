"""
Overall Intuition:
- This code uses Gemini through LangChain to analyze a product review.
- Instead of getting a normal text response, it uses structured output.
- The Review TypedDict defines the exact format we want from the model.
- The model should return three things: summary, sentiment, and pros.
- Annotated is used to give extra instruction/description for each field.
- Optional[list[str]] means pros can either be a list of strings or None.
- Finally, the code prints the complete structured result and then prints each field separately.
"""

from langchain_google_genai import ChatGoogleGenerativeAI  # Imports Gemini chat model class from LangChain
from dotenv import load_dotenv  # Imports load_dotenv to load API keys from the .env file
from typing import TypedDict,Annotated,Optional  # Imports TypedDict for structure, Annotated for field descriptions, and Optional for nullable values

load_dotenv()  # Loads environment variables like GOOGLE_API_KEY from the .env file

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")  # Creates a Gemini chat model object using gemini-2.5-flash

class Review(TypedDict):  # Defines the expected structure of the output dictionary
    
    summary:Annotated[str,"A brief summary of the review"]  # summary should be a string containing a short review summary
    sentiment:Annotated[str,"return sentiment of the review positive ,negative or neutral"]  # sentiment should be a string like positive, negative, or neutral
    pros:Annotated[Optional[list[str]],"write down all the pros inside a list"]  # pros should be a list of strings, or None if no pros are found

structured_model=model.with_structured_output(Review)  # Converts the normal chat model into a structured-output model following the Review schema

text="""This product exceeded my expectations with its solid build quality and easy setup.
The performance is reliable, and it handles everyday use without any issues.
I especially liked the intuitive design and user-friendly features.
Overall, it's a great value for the price and something I would recommend to others."""  # Stores the product review text that will be analyzed by the model

result=structured_model.invoke(text)  # Sends the review text to the model and gets output in the Review dictionary format

print(result)  # Prints the complete structured output dictionary
print('\n')  # Prints a blank line
print('\n')  # Prints another blank line
print(result['summary'])  # Prints only the summary field from the result
print('\n')  # Prints a blank line
print(result['sentiment'])  # Prints only the sentiment field from the result
print('\n')  # Prints a blank line
print(result['pros'])  # Prints only the pros field from the result
print('\n')  # Prints a blank line