import nltk
import pandas as pd
import matplotlib.pyplot as plt

tokens = ['the', 'rise', 'of', 'artificial', 'intelligence', 'has', 'led', 'to', 'significant', 'advancements', 'in', 'natural', 'language', 'processing', 'computer', 'vision',
          'and', 'other', 'fields', 'machine', 'learning', 'algorithms', 'are', 'becoming', 'more', 'sophisticated', 'enabling', 'computers', 'ware thought', 'once', 'to be',
          'the', 'exclusive', 'domain', 'the', 'to', 'perform', 'c complex', 't', 'tasks', 'that', "of", "humans", 'with', 'with', 'the', 'advent', 'of' 'deep', 'learning', 'neural',
          'networks', 'have', 'become' 'even', 'more', 'powerful', 'capable', 'of', 'processing', 'vast', 'amounts', 'of', 'data', 'and', 'learning', 'from', 'it', 'in', 'ways', 'that',
          'were' 'not', 'possible', 'before', 'as', 'a', 'result', 'ai', 'is', 'increasingly', 'being', 'used', 'in', 'a', 'wide', 'range', 'of', 'industries', 'from', 'healthcare', 'to', \
          'finance', 'to', 'transportation', 'and', 'its', 'impact', 'is', 'only', 'set', 'to', 'grow', 'in', 'the', 'years', 'to', 'come']

print(tokens)

unigrams = (pd.Series(nltk.ngrams(tokens, n=1)).value_counts())
print(unigrams)

print(unigrams[:10])

print(unigrams[:10].sort_values().plot.barh(color='lightsalmon', width=.9, figsize=(12, 8)))
plt.title("10 Most requently Occuring Unigrams")
plt.show()

biograms = (pd.Series(nltk.ngrams(tokens, n=2)).value_counts())
print(biograms[:10])

trigrams = (pd.Series(nltk.ngrams(tokens, 3)).value_counts())
print(trigrams[:10])