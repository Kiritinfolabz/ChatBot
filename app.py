import streamlit as st
from chatbot import chatbot_ui
from upload import upload_pdf_ui
from assistant import GenAI
from Documentation import doc

# Optional: Customizing the theme
st.set_page_config(page_title="LLM App", layout="wide",page_icon=":desktop_computer:")

def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose the app mode", ["Select","Chatbot", "Upload PDF","GenAI"])

    st.sidebar.markdown("""
    Choose any one
    """)
    if app_mode == "Select":
        doc()
    elif app_mode == "Chatbot":
        chatbot_ui()
    elif app_mode == "Upload PDF":
        upload_pdf_ui()
    elif app_mode == "GenAI":
        GenAI()


if __name__ == "__main__":
    main()
