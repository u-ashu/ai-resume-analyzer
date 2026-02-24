import pdfplumber
import io

def extract_text_from_pdf(file_bytes):
    text = ""
    
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    
    return text