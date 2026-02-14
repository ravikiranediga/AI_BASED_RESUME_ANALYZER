#Libraries
import PyPDF2
import docx

#Empty string to collect resume content
def extract_text(file):
    text=""
    if file.name.endswith(".pdf"):
        pdf=PyPDF2.PdfReader(file)

        for page in pdf.pages:
            text += page.extract_text()
            
    elif file.name.endswith(".docx"):
        doc= docx.Document(file)
        for para in doc.paragraphs:
            text +=para.text +" "
    return text.lower()