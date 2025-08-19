import json
import os
from langchain_community.document_loaders import PDFPlumberLoader
from langchain.schema import Document

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    return loader.load()




def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)  # Load the JSON data
    return data


def convert_json_to_documents(json_data):
    documents = []
    
    # Check if the JSON data is a list or a dictionary
    if isinstance(json_data, list):  # If the JSON is a list of records (patients)
        for record in json_data:
            # For each patient record, convert it into a Document
            doc_content = json.dumps(record)  # Convert dictionary to string for easier processing
            documents.append(Document(page_content=doc_content))
    
    elif isinstance(json_data, dict):  # If it's a single record (one patient)
        doc_content = json.dumps(json_data)  # Convert dictionary to string for easier processing
        documents.append(Document(page_content=doc_content))
    
    return documents

def convert_pdf_to_documents1(pdf_data):
    documents = []
    
    if isinstance(pdf_data, list):  # If the PDF data is a list of documents (multiple pages)
        for doc in pdf_data:
            # For each PDF document, convert it into a Document
            doc_content = doc.page_content  # Extract the page content
            documents.append(Document(page_content=doc_content))
    
    elif isinstance(pdf_data, Document):  # If it's a single document (one page)
        doc_content = pdf_data.page_content  # Extract the page content
        documents.append(Document(page_content=doc_content))
    
    return documents


def convert_pdf_to_documents(folder_path="rag_data"):
    documents = []
    
    # Get all PDF files from the folder
    if os.path.exists(folder_path):
        pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
        
        # Process each PDF file
        for pdf_file in pdf_files:
            pdf_path = os.path.join(folder_path, pdf_file)
            pdf_data = load_pdf(pdf_path)
            
            # Check if the PDF data is a list or a single document
            if isinstance(pdf_data, list):  # If the PDF data is a list of documents (multiple pages)
                for doc in pdf_data:
                    # For each PDF document, convert it into a Document
                    doc_content = doc.page_content  # Extract the page content
                    documents.append(Document(page_content=doc_content))
            
            elif isinstance(pdf_data, Document):  # If it's a single document (one page)
                doc_content = pdf_data.page_content  # Extract the page content
                documents.append(Document(page_content=doc_content))
    
    return documents