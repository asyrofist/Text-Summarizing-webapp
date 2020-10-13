from newspaper import fulltext
import requests
import spacy
article_url="https://analyticsindiamag.com/is-common-sense-common-in-nlp-models/ "
article = fulltext(requests.get(article_url).text)

spacy.load('en_core_web_md')

from summarizer import Summarizer
saloni = Summarizer()

result = saloni(article, min_length=30,max_length=300)
summary = "".join(result)
