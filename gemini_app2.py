import getpass
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Initialize the LLM with your Gemini model for translation
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",  # Adjust if using a specific translation model
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Create the prompt template for translation
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a translator that translates English text to Telugu."),
        ("human", "Translate the following to Telugu: {text}")
    ]
)

# Streamlit app layout
st.title("English to Telugu Translation with Gemini")
input_text = st.text_input("Enter English text here")  # Text input for English

# Output parser
output_parser = StrOutputParser()

# Chain the prompt with the LLM and output parser
chain = prompt | llm | output_parser

# Perform translation when there's input text
if input_text:
    translated_text = chain.invoke({'text': input_text})
    st.write("Translation:")
    st.write(translated_text)
