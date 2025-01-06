# LDA - Latent Dirichlet Allocation

import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import gensim
import gensim.corpora as corpora

data = pd.read_csv('news_articles.csv')
print(data.head())

print(data.info())

articles = data['content']

articles = articles.str.lower().apply(lambda x: re.sub(r"([^\w\s])", "", x))

# stop word removal
en_stopwords = stopwords.words('english')
articles = articles.apply(lambda x: ' '.join([word for word in x.split() if word not in (en_stopwords)]))

# tokenize
articles = articles.apply(lambda x: word_tokenize(x))

# stemming (done of speed as we have a lot of text
ps = PorterStemmer()
articles = articles.apply(lambda tokens: [ps.stem(token) for token in tokens])

print(articles)

dictionary = corpora.Dictionary(articles)
print(dictionary)

doc_term = [dictionary.doc2bow(text) for text in articles]
print(doc_term)

num_topics = 2

lda_model = gensim.models.LdaModel(corpus=doc_term,
                                   id2word=dictionary,
                                   num_topics=num_topics)

print(lda_model.print_topics(num_topics=num_topics, num_words=5))