from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains import RetrievalQA

def create_qa_system(combine_documents_chain, retriever):
    return RetrievalQA(combine_documents_chain=combine_documents_chain, retriever=retriever)
