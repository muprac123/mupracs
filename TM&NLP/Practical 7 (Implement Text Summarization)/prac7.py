from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Open the file and read the text
with open('F:/MSCPRACS/Sem3/TM&NLP/Practical 7 (Implement Text Summarization)/p7readtext.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Tokenize words and sentences
words = word_tokenize(text)
sents = sent_tokenize(text)
stopwords_set = set(stopwords.words('english'))

# Create frequency table
freqTable = {word.lower(): words.count(word) for word in set(words) if word.lower() not in stopwords_set}

# Calculate sentence values
sentValue = {sent: sum(freqTable.get(word.lower(), 0) for word in word_tokenize(sent)) for sent in sents}

# Calculate average score
avg = sum(sentValue.values()) / len(sents) if sents else 0

# Create summary based on average
summary = " ".join(sent for sent in sents if sent in sentValue and sentValue[sent] > 1.2 * avg)

print(summary)
