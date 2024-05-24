
from PyPDF2 import PdfReader
import requests
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdf_file.open('rb') as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


API_URL = "https://api-inference.huggingface.co/models/Falconsai/text_summarization"
headers = {"Authorization": "Bearer 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"}


def generate_summary(string_data):
    summary  = None

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    summary = query(string_data)
    
    
    return summary





