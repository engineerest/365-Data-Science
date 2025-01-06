# Import the relevant libraries

import numpy as np
from sklearn.model_selection import train_test_split

# Generate some data we are going to split

a = np.arange(1, 101)
# np.arange([start], [stop], [step]) returns evenly spaced values withing a given interval. By default the output in an ndarray
print(a)
b = np.arange(501, 601)
print(b)

# Split the data

# train_test_split(x) splits arrays or matrices into random train and test subsets
print(train_test_split(a))

# a_train, a_test = train_test_split(a, test_size=0.2, random_state=42)
# default value of shuffle is True
# random_state=42 - maybe state stop a random shuffling
# train_test_split(x, y) splits arrayS or matriceS into random train and test subsets
a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.2, random_state=42)

# Explore the result

print(a_train.shape, a_test.shape)
print(a_train)
print(a_test)
# Both arrays are shuffled!

# I don't like dedicating so much of my data to testing - Instructor

# Sometimes the order of the array is of utmost importance

# In practise, most of the time we prefer to shuffle the data
# Each time we run the code, we get a different shuffle

print(b_train.shape, b_test.shape)
print(b_train)
print(b_test)

# When we split 'a' and 'b' using the train_test_split, their elements are shuffled in the same way