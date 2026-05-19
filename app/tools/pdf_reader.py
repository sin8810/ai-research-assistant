from PyPDF2 import PdfReader

def read_pdf(file_path):

    try:
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted

        return text

    except Exception as e:
        return f"Error reading PDF: {e}"