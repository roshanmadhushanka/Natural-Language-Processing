# Stemming

from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
ss = SnowballStemmer()

example_words = ['python', 'Python', 'pythoning', 'pythoned', 'pythonly']

for w in example_words:
    print(ps.stem(w))