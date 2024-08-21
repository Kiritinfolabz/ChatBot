import streamlit as st
import os

UPLOAD_FOLDER = 'data'

# Create the upload directory if it does not exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join(UPLOAD_FOLDER, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except Exception as e:
        st.error(f"An error occurred while saving the file: {e}")
        return False

def upload_pdf_ui():
    st.header("Upload PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    if uploaded_file is not None:
        if save_uploaded_file(uploaded_file):
            st.success(f"File '{uploaded_file.name}' has been saved successfully!")
        else:
            st.error("Failed to save the file.")
