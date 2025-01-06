from nltk.stem import PorterStemmer

ps = PorterStemmer()

connect_tokens = ['connecting', 'connected', 'connectivity', 'connect', 'connects']

for t in connect_tokens:
    print(t, ": ", ps.stem(t))

learn_tokens = ['learning', 'learn', 'learns', 'learner', 'learnings']

for t in learn_tokens:
    print(t, ": ", ps.stem(t))

likes_tokens = ['likes', 'better', 'worse']

for t in likes_tokens:
    print(t, ": ", ps.stem(t))