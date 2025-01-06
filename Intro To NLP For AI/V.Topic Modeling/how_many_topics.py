from gensim.models.coherencemodel import CoherenceModel
from gensim.models import LsiModel
from lda_in_python import doc_term, dictionary, articles
import matplotlib.pyplot as plt

coherence_values = []
model_list = []

min_topics = 2
max_topics = 11

for num_topics_i in range(min_topics, max_topics+1):
    model = LsiModel(corpus=doc_term, id2word=dictionary, num_topics=num_topics_i)
    model_list.append(model)
    coherence_model = CoherenceModel(model=model, texts=articles, dictionary=dictionary, coherence='c_v')
    coherence_values.append(coherence_model.get_coherence())

plt.plot(range(min_topics, max_topics+1), coherence_values)
plt.show()

final_num_topics = 3
final_lsa_model = LsiModel(corpus=doc_term, id2word=dictionary, num_topics=final_num_topics)
print(final_lsa_model.print_topics(num_topics=final_num_topics, num_words=10))

