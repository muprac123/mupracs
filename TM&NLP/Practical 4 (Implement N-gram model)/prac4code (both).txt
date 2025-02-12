from nltk.util import ngrams

# Input sentence
sentence = "Natural language processing is a field of study focused on the interactions between human language and computers."

# Tokenize the sentence into words
words = sentence.split()

# Get user input for n
n = int(input("Enter the value of n for n-grams: "))

# Create n-grams from the list of words
ngrams_list = ngrams(words, n)

# Print the n-grams
for ngram in ngrams_list:
    print(ngram)
