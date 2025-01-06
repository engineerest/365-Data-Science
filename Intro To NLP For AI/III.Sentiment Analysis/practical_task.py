import pandas as pd
import numpy as np
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import transformers
from transformers import pipeline

data = pd.read_csv('book_reviews_sample.csv')
print(data.head())

print(data.info())

print(data['reviewText'][0])

data['reviewText_clean'] = data.apply(lambda x: re.sub(r"([^\w\s])", "", x['reviewText'].lower()), axis=1)

print(data.head())

vader_sentiment = SentimentIntensityAnalyzer()
data['vader_sentiment_score'] = data['reviewText_clean'].apply(lambda review: vader_sentiment.polarity_scores(review)['compound'])

print(data.head())


bins = [-1, -0.1, 0.1, 1]
names = ['negative', 'neutral', 'positive']

data['vader_sentiment_label'] = pd.cut(data['vader_sentiment_score'], bins, labels=names)

data['vader_sentiment_label'].value_counts().plot.bar()

transformer_pipeline = pipeline("sentiment_analysis")
transformer_labels = []

for review in data['reviewText_clean'].values:
    sentiment_list = transformer_pipeline(review)
    sentiment_label = [sent['label'] for sent in sentiment_list]
    transformer_labels.append(sentiment_label)

data['transformer_sentiment_label'] = transformer_labels

data['transformer_sentiment_label'].value_count().plot.bar()

