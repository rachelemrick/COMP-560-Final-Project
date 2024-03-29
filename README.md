Analyzing Partisan Bias in the News Using Sentiment Analysis
A final project for COMP 560 at UNC Chapel Hill
By Rachel Emrick, Trey Burgess, Winni Yong-Yu Yu, Tianjun Ma

Our project will use multiple APIs to gather and analyze articles/headlines from various news outlets to try to track partisan bias over time. 

First, we will use PyGoogleNews (https://docs.newscatcherapi.com/open-source/pygooglenews) to search for articles from various major news sources and gather their URLs.
Then, we will use Readability (https://pypi.org/project/readability-api/) to gather the plaintext of those articles. 
Finally, we will use Google Cloud Natural Language API (https://cloud.google.com/natural-language) to do the sentiment analysis on those articles/headlines (this one is still being decided on).
To check our model, we will use historical data from AllSides (https://www.allsides.com/media-bias) on media bias. 
