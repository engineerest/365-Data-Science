import nltk
# nltk.download('punkt') error
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize, sent_tokenize

sentences = "Her cat's name is Luna. Her dog's name is Max."

print(sent_tokenize(sentences))

sentence = "her cat's name is luna"
print(word_tokenize(sentence))

sentence_2 = "Her cat's name is Luna and her dog's name is max"
print(word_tokenize(sentence_2))
