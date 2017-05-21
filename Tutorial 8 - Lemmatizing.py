from nltk.stem import WordNetLemmatizer
import nltk


lemmatizer = WordNetLemmatizer()
word = ['running']
print(nltk.pos_tag(word))
print(lemmatizer.lemmatize(word[0]))