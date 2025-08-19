import streamlit as st
from langchain.schema import Document  
from text_splitter import split_text
from embedding_vectorstore import create_vector_store
from llm_setup import setup_llm
from qa_system import create_qa_system
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from rag_loader import convert_pdf_to_documents, load_pdf,load_json,convert_json_to_documents


st.title("📄 HR assistance System ")
st.markdown('###')

user_input = st.text_area("Enter your query:")

# documents = load_pdf('doc/int.pdf')
# json_docs=load_json('info.json')
# documents=convert_json_to_documents(json_data=json_docs)
documents=convert_pdf_to_documents()

    
split_documents = split_text(documents)


retriever = create_vector_store(split_documents)

# llm_chain = setup_llm()
llm_chain = setup_llm(model='gemma3:1b')
combine_documents_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="context")

qa_system = create_qa_system(combine_documents_chain, retriever)


if user_input:
    response = qa_system(user_input)["result"]
    st.write("**Response**")
    st.write(response)
