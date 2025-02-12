import nltk
nltk.download('averaged_perceptron_tagger')
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer
words=['run','runner','running','ran','runs','easily','caring']

ps=PorterStemmer()
print("Porter Stemmer")
for word in words:
    print(word,'----->',ps.stem(word))


snowball=SnowballStemmer(language='english')
print("Snowball Stemmer")
for word in words:
    print(word,'----->',snowball.stem(word))
    

lancaster=LancasterStemmer()
print("Lancaster Stemmer")
for word in words:
    print(word,'----->',lancaster.stem(word))



