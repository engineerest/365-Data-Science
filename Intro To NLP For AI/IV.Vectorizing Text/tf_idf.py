from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

data =[
    'Most shark attacks occur about 10 feet from the beach since that is where the people are',
    'the efficiency with which he paired the socks in the drawer was quite admirable',
    'carol drank the blood as if she were a vampire',
    'giving directions that the mountains are to the west only works when you can see them',
    'the sign said there was road work ahead so he decided to speed up',
    'the gruff old man sat in the back of the bait shop grumbling to himself as he scooped out a handful of worms'
    ]

tfidfvec = TfidfVectorizer()
tfidfvec_fit = tfidfvec.fit_transform(data)

tfidf_bag = pd.DataFrame(tfidfvec_fit.toarray(), columns=tfidfvec.get_feature_names_out())
print(tfidf_bag)