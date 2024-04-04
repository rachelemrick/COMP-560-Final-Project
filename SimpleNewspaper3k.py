import requests
from newspaper import Article
from bs4 import BeautifulSoup
from textblob import TextBlob
import nltk
nltk.download('punkt')

feed = 'https://abcnews.go.com/abcnews/politicsheadlines'
response = requests.get(feed)

webpage = response.content
soup = BeautifulSoup(webpage, features="xml")

items = soup.findAll('item')

articles = []
for item in items:
    link = item.find('link').text
    articles.append(link)

print("Number of articles: ", len(articles))
poliarities = []
subjectivities = []

for url in articles:
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    title = article.title
    summary = article.summary
    keywords = article.keywords
    publish_date = article.publish_date
    text = article.text
    text_blob = TextBlob(text)
    sentiment = text_blob.sentiment
    subjectivity = text_blob.subjectivity
    poliarity = text_blob.polarity

    print("************")
    print("Title: ", title)
    print("url: ", url)
    print("publish date: ", publish_date)
    print("Keywords: ", keywords)
    print(f"Sentiment: {sentiment}")
    poliarities.append(poliarity)
    subjectivities.append(subjectivity)
    #print("Summary: ", summary)
    
print("Average Polarity: ", sum(poliarities)/len(poliarities))
print("Average Subjectivity: ", sum(subjectivities)/len(subjectivities))
