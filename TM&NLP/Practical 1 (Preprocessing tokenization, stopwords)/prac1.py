import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Tokenization example
text = "God is Great! I won a lottery."
print("The words are:", word_tokenize(text))
print("The sentences are:", sent_tokenize(text))

# English stop words removal example
text = "This is an example sentence showing the removal of stop words."
tokens = word_tokenize(text)
print("Tokens:", tokens)

stop_words = set(stopwords.words('english'))
print("Stop Words:", stop_words)

filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("Filtered Tokens:", filtered_tokens)
