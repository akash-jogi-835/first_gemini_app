import getpass
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Initialize the LLM with your Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Create the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a chatbot"),  # System type message
        ("human", "Question: {question}")  # Human type message
    ]
)

# Streamlit app layout
st.title("Langchain Demo With Gemini")
input_text = st.text_input("Enter Your Question Here")  # Corrected method

# Output parser
output_parser = StrOutputParser()

# Chain the prompt with the LLM and output parser
chain = prompt | llm | output_parser

# Invoke the chain when there's input text
if input_text:
    st.write(chain.invoke({'question': input_text}))
