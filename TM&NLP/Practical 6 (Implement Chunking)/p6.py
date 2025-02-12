import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Step 1: Tokenize the sentence into words
words = word_tokenize(sentence)

# Step 2: Apply Part-of-Speech (POS) tagging
pos_tags = pos_tag(words)

# Step 3: Define a chunk grammar (chunk pattern)
# This grammar chunks sequences of adjectives (JJ) and nouns (NN) together
chunk_grammar = r"""
    NP: {<DT>?<JJ>*<NN>}   # Chunk determiner, adjective(s), and noun
"""

# Step 4: Create a chunk parser using the defined grammar
chunk_parser = RegexpParser(chunk_grammar)

# Step 5: Parse the POS-tagged sentence to find chunks
chunk_tree = chunk_parser.parse(pos_tags)

# Step 6: Visualize the chunk tree (optional)
chunk_tree.pretty_print()

# To view the chunked phrases in the sentence
for subtree in chunk_tree.subtrees(filter=lambda t: t.label() == 'NP'):
    print("Chunked phrase:", " ".join(word for word, pos in subtree.leaves()))
