# Remove stopping words

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "This is an example showing off stop word filteration"
stop_words = stopwords.words("english")
words = word_tokenize(example)

filtered_sentence = [w for w in words if w not in stop_words]

print(filtered_sentence)

