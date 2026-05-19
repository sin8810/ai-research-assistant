import yake

def extract_keywords(text, num_keywords=5):

    kw_extractor = yake.KeywordExtractor(top=num_keywords)

    keywords = kw_extractor.extract_keywords(text)

    return [keyword[0] for keyword in keywords]