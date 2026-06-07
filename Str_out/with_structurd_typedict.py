from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Review(TypedDict):
    
    summary:Annotated[str,"A brief summary of the review"]
    sentiment:Annotated[str,"return sentiment of the review positive ,negative or neutral"]
    pros:Annotated[Optional[list[str]],"write down all the pros inside a list"]

structured_model=model.with_structured_output(Review)
text="""This product exceeded my expectations with its solid build quality and easy setup.
The performance is reliable, and it handles everyday use without any issues.
I especially liked the intuitive design and user-friendly features.
Overall, it's a great value for the price and something I would recommend to others."""

result=structured_model.invoke(text)
print(result)
print('\n')
print('\n')
print(result['summary'])
print('\n')
print(result['sentiment'])
print('\n')
print(result['pros'])
print('\n')