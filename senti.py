from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt')

url='https://www.ndtv.com/video/news/news/world-far-more-complicated-place-today-says-s-jaishankar-720829#livevideo-featured'
article=Article(url)

article.download()
article.parse()
article.nlp()

text=article.summary
print(text)

blob=TextBlob(text)
sentiment=blob.sentiment.polarity

print(sentiment)