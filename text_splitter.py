from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings

def split_text(documents):
    text_splitter = SemanticChunker(HuggingFaceEmbeddings())
    return text_splitter.split_documents(documents)
