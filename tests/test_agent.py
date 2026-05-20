import sys
import os

sys.path.append(os.path.abspath("app"))

from agent import process_document

def test_process_document():

    result = process_document("../sample_data/sample.pdf")

    assert result is not None
    assert "SUMMARY" in result