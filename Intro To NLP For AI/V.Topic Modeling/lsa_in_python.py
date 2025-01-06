# LSA - Latent Semantic Analysis
import gensim
from gensim.models import LsiModel

from lda_in_python import doc_term, dictionary, num_topics

lsa_model = LsiModel(corpus=doc_term,
                     id2word=dictionary,
                     num_topics=num_topics)

print(lsa_model.print_topics(num_topics=num_topics, num_words=5))

