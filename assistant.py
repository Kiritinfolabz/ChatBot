import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
import os

# Load environment variables
load_dotenv()
def GenAI():
# Load the GROQ and Google API keys~~~
    groq_api_key = os.getenv("GROQ_API_KEY")
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

    prompt = ChatPromptTemplate.from_messages(
            [
            ("system","You are a helpful assistant. Please response to the user queries"),
            ("user","Question:{question}")
        ]
    )

    st.title("LLM Model")
    input_text = st.text_input("Ask anything")

    llm = ChatGroq(model="Llama3-8b-8192")
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser

    if input_text:
        st.write(chain.invoke({"question":input_text}))