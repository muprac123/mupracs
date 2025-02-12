import nltk

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

from collections import Counter

text = "Guru(9 is one of the best sites to learn WEB, SAP, Ethical Hacking and much more online."
lower_case = text.lower()
tokens = nltk.word_tokenize(lower_case)
tags = nltk.pos_tag(tokens)
print(tags)

counts = Counter(tag for word, tag in tags)
print(counts)

fd = nltk.FreqDist(tokens)
fd.plot()

fd1 = nltk.FreqDist(counts)
fd1.plot()
