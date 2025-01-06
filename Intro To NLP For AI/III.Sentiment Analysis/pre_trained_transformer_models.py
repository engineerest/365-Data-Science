import transformers
from transformers import pipeline

sentence_1 = 'i had a great time a the movie it was really funny'
sentence_2 = 'i had a great time at the movie but the parking was terrible'
sentence_3 = 'i had a great time at the movie but the parking wasn\'t great'
sentence_4 = 'i went to see a movie'


sentiment_pipeline = pipeline("sentiment-analysis")

print(sentence_1)
print(sentiment_pipeline(sentence_1))

print(sentence_2)
print(sentiment_pipeline(sentence_2))

print(sentence_3)
print(sentiment_pipeline(sentence_3))

print(sentence_4)
print(sentiment_pipeline(sentence_4))

specific_model = pipeline('sentiment-analysis', model='finiteautomata/bertweet-base-sentiment-analysis')

print(sentence_1)
print(sentiment_pipeline(sentence_1))

print(sentence_2)
print(sentiment_pipeline(sentence_2))

print(sentence_3)
print(sentiment_pipeline(sentence_3))

print(sentence_4)
print(sentiment_pipeline(sentence_4))


