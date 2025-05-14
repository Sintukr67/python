#import pandas library
#it provides easy to use data structure for data analysis

#import nltk library
#it is a library which is used to process human language

#nltk provide sentiment analysis of human data
#sentiment analysis involve working out wheather a piece of text is positive ,negative or neutral

#we will use VADER
#VADER is the valance aware dictionary and sentiment reasoner
#it also takes into account the intensity of the sentiment


import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vender_lexicon')
file=(r'C:\python\pandas\earning.csv')
xl=pd.ExcelFile(file)
dfs=xl.parse(xl.sheet_name[0])
dfs=list(dfs['Timeline'])
print(dfs)
