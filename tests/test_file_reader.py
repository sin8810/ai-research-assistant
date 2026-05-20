import sys
import os

sys.path.append(os.path.abspath("app"))

from tools.file_reader import read_text_file

def test_read_text_file():

    content = read_text_file("sample_data/research_notes.txt")

    assert content is not None
    assert len(content) > 0