import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("AI-Powered Data Query Interface for 👕 Database")

question = st.text_input("Query: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)






