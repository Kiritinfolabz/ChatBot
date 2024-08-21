import streamlit as st
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

# Load the GROQ and Google API keys
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def chatbot_ui():
    st.header("DOCUMENT Question & Answer")

    # Initialize the LLM
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

    # Define the prompt template
    prompt_template = """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question.
    <context>
    {context}
    </context>
    Questions: {input}
    """

    prompt = ChatPromptTemplate.from_template(prompt_template)

    def vector_embedding():
        if "vectors" not in st.session_state:
            # Set up embeddings and document loader
            st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            st.session_state.loader = PyPDFDirectoryLoader("data")
            
            # Load documents
            st.session_state.docs = st.session_state.loader.load()
            
            # Split documents into chunks
            st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:20])
            
            # Create FAISS vector store from documents
            st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

    # Input for the user's question
    prompt1 = st.text_input("Enter Your Question From Documents")
    
    # Button to initialize document embeddings
    if st.button("Documents Embedding"):
        try:
            vector_embedding()
            st.write("Vector Store DB Is Ready")
        except:
            st.error(f"Error in creating vector embeddings")

    # Processing the question if provided
    if prompt1:
        try:
            document_chain = create_stuff_documents_chain(llm, prompt)
            retriever = st.session_state.vectors.as_retriever()
            retrieval_chain = create_retrieval_chain(retriever, document_chain)
            
            start = time.process_time()
            response = retrieval_chain.invoke({'input': prompt1})
            response_time = time.process_time() - start
            
            st.write("Response time:", response_time)
            st.write(response['answer'])
            
            # Display similar documents
            with st.expander("Document Similarity Search"):
                for i, doc in enumerate(response["context"]):
                    st.write(doc.page_content)
                    st.write("--------------------------------")
        except:
            st.warning(f"CLICK ON THE BUTTON TO CHECK OUTPUT")

if __name__ == "__main__":
    chatbot_ui()
