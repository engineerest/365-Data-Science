sentence = "Her cat's name is Luna"

lower_sentence = sentence.lower()
print(lower_sentence)

sentence_list = ['Could you pass me the TV remote?',
                 'It is IMPOSSIBLE to find this hotel',
                 'Want to go for dinner on Tuesday']

lower_sentence_list = [x.lower() for x in sentence_list]
print(lower_sentence_list)