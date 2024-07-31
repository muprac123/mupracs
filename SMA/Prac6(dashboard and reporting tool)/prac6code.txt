import pandas as pd
import snscrape.modules.twitter as sntwitter
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import string
import re
import textblob
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
from wordcloud import ImageColorGenerator
import warnings
import os

# Download NLTK resources
nltk.download('stopwords')

# Set up matplotlib to work interactively
%matplotlib inline

# Using os library to call CLI commands in python
os.system("snscrape --jsonl --max-results 10000 --since 2023-03-13 twittersearch 'CHATGPT4' > text-chatGPT4-tweets.json")

# Create a pandas dataframe
tweets_df_chatGPT4 = pd.read_json('text-chatGPT4-tweets.json', lines=True)

# Select relevant columns
df_chatGPT4 = tweets_df_chatGPT4[["date", "rawContent", "renderedContent", "user", "replyCount", "retweetCount", "likeCount", "lang", "place", "hashtags", "viewCount"]]

# Remove duplicates
df2 = df_chatGPT4.drop_duplicates('renderedContent')

# Shape of DataFrame
print(df2.shape)
df2.head()
df2.info()
df2.date.value_counts()

# Heatmap for missing values
plt.figure(figsize=(17, 5))
sns.heatmap(df2.isnull(), cbar=True, yticklabels=False)
plt.xlabel("Column_Name", size=14, weight="bold")
plt.title("Places of missing values in column", fontweight="bold", size=17)
plt.show()
