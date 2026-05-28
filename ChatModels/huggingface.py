"""
Overall Intuition:
- This code loads a Hugging Face model using LangChain.
- It creates a text-generation pipeline using TinyLlama.
- Then it wraps that pipeline as a chat model.
- Finally, it asks a question and prints the generated answer.
"""

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline  # Imports LangChain classes for using Hugging Face models

llm = HuggingFacePipeline.from_model_id(  # Creates a Hugging Face pipeline-based LLM using a model ID
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # Specifies the Hugging Face model to load
    task="text-generation",  # Tells the model to perform text generation
    pipeline_kwargs={  # Provides extra settings for the generation pipeline
        "temperature": 0.5,  # Controls randomness of output; lower means more focused
        "max_new_tokens": 100  # Limits the number of new tokens generated
    }
)

model = ChatHuggingFace(llm=llm)  # Wraps the Hugging Face pipeline so it can work like a chat model

result = model.invoke("What is the capital of India?")  # Sends the question to the model and stores the response

print(result.content)  # Prints only the final text content of the response