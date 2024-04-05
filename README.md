#Analyzing Partisan Bias in the News Using Sentiment Analysis

##A final project for COMP 560 at UNC Chapel Hill

By Rachel Emrick, Trey Burgess, Winni Yong-Yu Yu, Tianjun Ma

Our project will use multiple APIs to gather and analyze articles from various news outlets to try to track partisan bias over time. 

First, we will use the NewsCatcher API (https://www.newscatcherapi.com/) to search for articles over the past 20 years or so from various major news sources and gather their URLs. 

Then, we will use Newspaper3k (https://newspaper.readthedocs.io/en/latest/) to gather the plaintext of those articles.

Finally, we will use NLTK (https://www.nltk.org/) to do the sentiment analysis on those articles.

To check our model, we will use historical data from AllSides (https://www.allsides.com/media-bias) on media bias.