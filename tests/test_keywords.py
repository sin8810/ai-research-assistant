import sys
import os

sys.path.append(os.path.abspath("app"))

from tools.keyword_extractor import extract_keywords

def test_keyword_extraction():

    text = "Artificial intelligence improves automation and decision making."

    keywords = extract_keywords(text)

    assert keywords is not None
    assert len(keywords) > 0