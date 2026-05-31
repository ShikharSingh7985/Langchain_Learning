from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage


chattemplate = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful {domain} expert"),
    ("human", "explain in simple terms what is {topic}")
])


promppt=chattemplate.invoke({'domain':'cricket','topic':'top spin'})

print(promppt)