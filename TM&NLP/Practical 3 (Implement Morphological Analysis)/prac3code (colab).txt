import spacy
from nltk.stem import PorterStemmer

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Define sentences
interrogative_sentence = "What is the weather like today?"
declarative_sentence = "The weather is sunny."
complex_sentence = "I went to the store, but they were closed, so I had to go to another store."

# Process sentences using spaCy
interrogative_doc = nlp(interrogative_sentence)
declarative_doc = nlp(declarative_sentence)
complex_doc = nlp(complex_sentence)

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# Function to print tokens, their part of speech, lemmatization, and stemming
def print_tokens_with_stemming_and_lemmatization(doc):
    for token in doc:
        stemmed = stemmer.stem(token.text)  # Apply stemming
        lemmatized = token.lemma_  # Apply lemmatization
        print(f"Token: {token.text}, POS: {token.pos_}, Lemma: {lemmatized}, Stemmed: {stemmed}")
    print("\n")

# Print results for each sentence
print("Interrogative Sentence Analysis:")
print_tokens_with_stemming_and_lemmatization(interrogative_doc)

print("Declarative Sentence Analysis:")
print_tokens_with_stemming_and_lemmatization(declarative_doc)

print("Complex Sentence Analysis:")
print_tokens_with_stemming_and_lemmatization(complex_doc)
