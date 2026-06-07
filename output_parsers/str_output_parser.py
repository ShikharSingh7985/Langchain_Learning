import os
import warnings
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser  # <-- Added for clean output

# Optional: Suppress noisy transformers warnings in the console
warnings.filterwarnings("ignore", category=UserWarning)
os.environ["TOKENIZERS_PARALLELISM"] = "false"

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
   
)
model = ChatHuggingFace(llm=llm)

# Use StrOutputParser to strip chat structural tokens (<|user|>, <|assistant|>) automatically
clean_chain = model | StrOutputParser()

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

# Run the first prompt
prompt1 = template1.invoke({'topic': 'Avengers'})
result1_content = clean_chain.invoke(prompt1)

# FIX: Remove the quotes around result1_content so it passes the actual generated text!
prompt2 = template2.invoke({'text': result1_content})
result2_content = clean_chain.invoke(prompt2)

print("--- Final Summary ---")
print(result2_content)