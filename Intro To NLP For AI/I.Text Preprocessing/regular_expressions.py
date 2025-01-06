import re

# my_folder = "C:\Users\User\Desktop" bad, error
my_folder = r"C:\Users\User\Desktop"
print(my_folder)

result_search = re.search("pattern", r"string to contain the pattern")
# re.search(word, text) - looks for word in received text
print(result_search)

result_search_2 = re.search("pattern", r"the phrase to find isn't in this string")
print(result_search_2)

string = r"sara was able to help me find the items I needed quickly"

new_string = re.sub("sara", "sarah", string)
# re.sub(word1, word2) - changes the meaning of word1
print(new_string)

customer_reviews = ["sam was a great help to me in the store",
                    "the cashier was very rude to me, I think her name was eleanor",
                    "amazing work from sadeen!",
                    "sarah was able to help me find the items I needed quickly",
                    "lucy is such a great addition to the team",
                    "great service from sara she found me what i wanted"
                    ]

sarahs_reviews = []

pattern_to_find = r"sarah?"

for string in customer_reviews:
    if (re.search(pattern_to_find, string)):
        sarahs_reviews.append(string)

print(sarahs_reviews)

a_reviews = []
pattern_to_find = r"^a"

for string in customer_reviews:
    if (re.search(pattern_to_find, string)):
        a_reviews.append(string)

print(a_reviews)

y_reviews = []
pattern_to_find = r"y$"

for string in customer_reviews:
    if (re.search(pattern_to_find, string)):
        y_reviews.append(string)

print(y_reviews)

needwant_reviews = []
pattern_to_find = r"(need|want)ed"

for string in customer_reviews:
    if (re.search(pattern_to_find, string)):
        needwant_reviews.append(string)

print(needwant_reviews)

no_punct_reviews = []
pattern_to_find = r"[^\w\s]"

for string in customer_reviews:
    no_punct_string = re.sub(pattern_to_find, "", string)
    no_punct_reviews.append(no_punct_string)

print(no_punct_reviews)