import spacy
from spacy import displacy
from spacy import tokenizer
import re

nlp = spacy.load("en_core_web_sm")

google_text = "Google was founded on September 4, 1998, by computer scientists Larry Page and Sergey Brin while they were PhD stud ents at Stanford University in California. Together they own about 14% of its publicly listed shares and control 5 6% of its stockholder voting power through super-voting stock. The company went public via an initial public offeri ng (IPO) in 2004. In 2015, Google was reorganized as a wholly owned subsidiary of Alphabet Inc. Google is Alphabet s largest subsidiary and is a holding company for Alphabet's internet properties and interests. Sundar Pichai was a ppointed CEO of Google on October 24, 2015, replacing Larry Page, who became the CEO of Alphabet. On December 3, 20 19, Pichai also became the CEO of Alphabet."
print(google_text)

spacy_doc = nlp(google_text)

for word in spacy_doc.ents:
    print(word.text, word.label_)

displacy.render(spacy_doc, style="ent", jupyter=True)

google_text_clean = re.sub(r'[^\w\s]', '', google_text).lower()
print(google_text_clean)

spacy_doc_clean = nlp(google_text_clean)

for word in spacy_doc_clean.ents:
    print(word.text, word.label_)

displacy.render(spacy_doc_clean, style="ent", jupyter=True)