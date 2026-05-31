"""
Overall Intuition:
- This code creates a simple terminal-based chatbot using Google Gemini through LangChain.
- It keeps storing the full conversation inside chat_history.
- The system message gives the assistant its role.
- Every user message is added to chat_history.
- Gemini receives the complete chat_history, so it can answer with previous context.
- The AI response is also added back into chat_history.
- The loop continues until the user types 'exit'.
"""

from langchain_google_genai import ChatGoogleGenerativeAI  # Imports the Gemini chat model class from LangChain
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage  # Imports message classes for system, user, and AI messages

from dotenv import load_dotenv  # Imports load_dotenv to load API keys from the .env file

load_dotenv()  # Loads environment variables like GOOGLE_API_KEY from the .env file


model= ChatGoogleGenerativeAI(model="gemini-2.5-flash")  # Creates a Gemini chat model object using gemini-2.5-flash

chat_history=[  # Creates a list to store the complete conversation history
    SystemMessage(content='You are a helpful Assistant')  # Adds a system message that defines how the AI should behave
]


while True:  # Starts an infinite loop so the chatbot keeps running until we manually break it
    user_input=input('You :- ')  # Takes input from the user in the terminal
    chat_history.append(HumanMessage(content=user_input))  # Adds the user's message to chat_history
    if user_input=='exit':  # Checks if the user typed exit
        break  # Stops the loop if user_input is exit
    
    result=model.invoke(chat_history)  # Sends the full conversation history to Gemini and gets the AI response
    chat_history.append(AIMessage(content=result.content))  # Adds the AI response to chat_history for future context
    print('AI:-' ,result.content)  # Prints the AI response in the terminal
    
print(chat_history)  # Prints the final complete chat history after the loop ends