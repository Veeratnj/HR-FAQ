from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store(documents,save_path='vector_store'):
    embedder = HuggingFaceEmbeddings()
    vector_store = FAISS.from_documents(documents, embedder)
    vector_store.save_local(save_path)
    return vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
