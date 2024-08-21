import streamlit as st

# Project documentation content
def doc():
    PROJECT_DESCRIPTION = """
    # Project Title: QA Chatbot

    ## Overview
    This project involves creating a chatbot that allows users to upload a PDF and ask questions about its content. The chatbot processes the PDF and provides answers based on the text extracted from the PDF.

    ## Features
    - **PDF Upload**: Users can upload PDF documents.
    - **Question Answering**: Users can ask questions related to the content of the uploaded PDF.
    - **Model Results**: A separate tab to load a model and generate results from an API.

    ## Technologies Used
    - **Streamlit**: For the web interface.
    - **PyMuPDF**: For PDF processing.
    - **Transformers**: For the question-answering model.
    - **OpenAI GPT-3**: For language processing.
    - **API Integration**: For model results.

    ## How to Use
    1. Upload a PDF document.
    2. Ask any question related to the uploaded document.
    3. View the model results in the dedicated tab.
    4. Read the project documentation in the 'About' tab.

    ## Future Work
    - Enhance PDF processing for better text extraction.
    - Add support for more file formats.
    - Improve the accuracy of the question-answering model.

    ## Acknowledgements
    - Thanks to the open-source community for the tools and libraries.
    """

    # Main function to create the About tab and render content
    def main():
        st.title("Question Answer Chatbot Project")
        st.markdown(PROJECT_DESCRIPTION)

    main()

# Call the doc function to run the app
