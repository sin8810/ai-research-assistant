from tools.file_reader import read_text_file
from tools.pdf_reader import read_pdf
from tools.keyword_extractor import extract_keywords
from tools.summarizer import summarize_text
import os

def process_document(file_path):

    try:

        # Detect file type
        file_extension = os.path.splitext(file_path)[1]

        # Read content
        if file_extension == ".txt":
            content = read_text_file(file_path)

        elif file_extension == ".pdf":
            content = read_pdf(file_path)

        else:
            return "Unsupported file type."

        # Check empty content
        if not content:
            return "File is empty."

        # Extract keywords
        keywords = extract_keywords(content)

        # Generate summary
        summary = summarize_text(content)

        # Final output
        result = f"""

==============================
AI RESEARCH ASSISTANT
==============================

FILE: {file_path}

------------------------------
SUMMARY
------------------------------

{summary}

------------------------------
KEYWORDS
------------------------------
"""

        for keyword in keywords:
            result += f"- {keyword}\n"

        return result

    except Exception as e:
        return f"Error processing document: {e}"