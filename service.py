import pdfplumber
from io import BytesIO
import streamlit as st


def extract_text_from_pdf(pdf_file):
    try:
        with pdfplumber.open(pdf_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ''