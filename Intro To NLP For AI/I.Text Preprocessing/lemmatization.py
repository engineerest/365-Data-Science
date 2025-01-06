import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

from stemming import connect_tokens, learn_tokens, likes_tokens

lemmatizer = WordNetLemmatizer()

for t in connect_tokens:
    print(t, ": ", lemmatizer.lemmatize(t))

for t in learn_tokens:
    print(t, ": ", lemmatizer.lemmatize(t))

for t in likes_tokens:
    print(t, ": ", lemmatizer.lemmatize(t))