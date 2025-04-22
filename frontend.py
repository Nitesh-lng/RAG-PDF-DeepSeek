'''Step-1. Steup upload PDF'''
from Rag_pipeline import answer_query, retrieve_docs, llm_model
import os
import streamlit as st

uploaded_file = st.file_uploader("Choose a PDF file",
                                 type="pdf",
                                 )  



user_query=st.text_input("Ask a question about the PDF file",placeholder="Type your question here...")
ask_question = st.button("Ask")

if ask_question:
    if uploaded_file:  
        
        st.chat_message("user").write('user_query')
        
        retrieved_docs=retrieve_docs(user_query)
        response=answer_query(documents=retrieved_docs, model=llm_model, query=user_query)
        st.chat_message("AI Lawyer").write(response)
    
    else:
        st.error("Please upload a PDF file to ask a question.")
        
        