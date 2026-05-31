"""
Overall Intuition:
- This code creates a chat prompt template for a customer support chatbot.
- The template contains three parts: system message, previous chat history, and current user query.
- Previous chat history is read from a text file and stored in a list.
- Then the chat template is filled using that chat history and the new query.
- Finally, it prints the raw chat history and the final generated prompt structure.
"""

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder  # Imports ChatPromptTemplate for creating chat prompts and MessagesPlaceholder for inserting chat history

chattemplate = ChatPromptTemplate.from_messages([  # Creates a chat prompt template using a list of messages
    ("system", "you are a helpful customer support agent"),  # Adds a system message that defines the assistant's role
    MessagesPlaceholder(variable_name='chat_history'),  # Reserves a placeholder where previous chat history will be inserted
    ("human", "{query}")  # Adds the current human/user message using the query variable
])

chat_history=[]  # Creates an empty list to store previous chat messages

with open('Langchain_prompts/chat_history.txt', 'r', encoding='utf-8') as f:  # Opens the chat history text file in read mode using UTF-8 encoding
   chat_history.extend( f.readlines())  # Reads all lines from the file and adds them to the chat_history list
   
print(chat_history)  # Prints the chat history list loaded from the file

prompt=chattemplate.invoke({'chat_history':chat_history,'query':'where is my refund'})  # Fills the template with chat history and current query

print(prompt)  # Prints the final prompt object created by the chat template