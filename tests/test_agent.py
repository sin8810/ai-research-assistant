import sys
import os

sys.path.append(os.path.abspath("app"))

from agent import process_document


def test_process_document():

    result = process_document("sample_data/sample.pdf")

    assert result is not None
    assert "SUMMARY" in result


def test_missing_file():

    result = process_document("sample_data/fake.pdf")

    assert result == "Error: File does not exist."


def test_unsupported_file():

    result = process_document("sample_data/test.docx")

    assert result == "Error: Unsupported file type."