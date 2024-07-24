import streamlit as st
from langchain.llms import OpenAI

st.title("Basic AI APP")

openai_api_key = st.sidebar.text_input("OpenAI API KEY")

def response(text):

    llm = OpenAI(temperature = 0.5,
                 openai_api_key=openai_api_key)
    st.info(llm(text))

with st.form("FORM"):
    text = st.text_area("Enter your text:", "Any question?")

    submitted = st.form_submit_button("Enter")

    if not openai_api_key.startswith("sk-"):
        st.warning("Wrong API KEY!!!")
    if submitted and openai_api_key.startswith("sk-"):
        response(text)
