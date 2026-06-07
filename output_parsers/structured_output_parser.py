import os
import warnings
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, ResponseSchema


load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")



# 1st Prompt -> detailed explanation
template1 = PromptTemplate(
    template="Write a detailed explanation on {topic}",
    input_variables=['topic']
)

# 2nd Prompt -> summary
template2 = PromptTemplate(
    template="Write a 5 line summary on this text:\n\n{text}",
    input_variables=['text']
)


parser=StrOutputParser()

chain=template1 | model | template2 | model | parser

result=chain.invoke({'topic':'Apple company'})

print(result)