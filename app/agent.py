from tools.file_reader import read_text_file
from tools.pdf_reader import read_pdf
from tools.keyword_extractor import extract_keywords
from tools.summarizer import summarize_text

import os


def process_document(file_path):

    try:

        # Check if file exists
        if not os.path.exists(file_path):
            return "Error: File does not exist."

        # Detect file type
        file_extension = os.path.splitext(file_path)[1].lower()

        # Read content
        if file_extension == ".txt":

            content = read_text_file(file_path)
            file_type = "Text File"

        elif file_extension == ".pdf":

            content = read_pdf(file_path)
            file_type = "PDF Document"

        else:
            return "Error: Unsupported file type."

        # Check empty content
        if not content or len(content.strip()) == 0:
            return "Error: File is empty."

        # Extract keywords
        keywords = extract_keywords(content)

        # Generate summary
        summary = summarize_text(content)

        # Final formatted output
        result = f"""

========================================
     AI ACADEMIC RESEARCH ASSISTANT
========================================

FILE NAME:
{os.path.basename(file_path)}

FILE TYPE:
{file_type}

========================================
SUMMARY
========================================

{summary}

========================================
KEYWORDS
========================================
"""

        for keyword in keywords:
            result += f"\n• {keyword}"

        result += "\n\n========================================"

        return result

    except Exception as e:

        return f"System Error: {e}"