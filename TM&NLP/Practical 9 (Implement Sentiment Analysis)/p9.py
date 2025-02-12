# Importing necessary libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the necessary resources
nltk.download('vader_lexicon')

# Create a SentimentIntensityAnalyzer object
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment of text
def analyze_sentiment(text):
    # Perform sentiment analysis
    sentiment_scores = sia.polarity_scores(text)
   
    # Interpret the results
    if sentiment_scores['compound'] >= 0.05:
        return "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Example usage
text = "I love this product! It's amazing."
result = analyze_sentiment(text)
print(f"Sentiment: {result}")
