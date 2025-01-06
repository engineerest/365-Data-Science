import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

data =[
    'Most shark attacks occur about 10 feet from the beach since that is where the people are',
    'the efficiency with which he paired the socks in the drawer was quite admirable',
    'carol drank the blood as if she were a vampire',
    'giving directions that the mountains are to the west only works when you can see them',
    'the sign said there was road work ahead so he decided to speed up',
    'the gruff old man sat in the back of the bait shop grumbling to himself as he scooped out a handful of worms'
    ]


countvec = CountVectorizer()

countvec_fit = countvec.fit_transform(data)

bag_of_words = pd.DataFrame(countvec_fit.toarray(), columns=countvec.get_feature_names_out())
print(bag_of_words)

