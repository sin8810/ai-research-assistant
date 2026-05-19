from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text, sentence_count=3):

    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))

        summarizer = LsaSummarizer()

        summary = summarizer(parser.document, sentence_count)

        final_summary = ""

        for sentence in summary:
            final_summary += str(sentence) + " "

        return final_summary

    except Exception as e:
        return f"Error generating summary: {e}"