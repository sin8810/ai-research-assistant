from tools.pdf_reader import read_pdf
from tools.summarizer import summarize_text

file_path = "sample_data/sample.pdf"

content = read_pdf(file_path)

summary = summarize_text(content)

print("\nAI SUMMARY:\n")

print(summary)