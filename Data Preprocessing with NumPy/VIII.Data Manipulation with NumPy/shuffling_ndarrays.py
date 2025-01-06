import numpy as np

# Shuffling Data

lending_co_data_numeric = np.genfromtxt("Lending-company-Numeric.csv", delimiter=',')
print(lending_co_data_numeric)

# Shuffling
# Rearranging the parts of a dataset

# We do so without a fixed pattern

# The end goal is that a random sample
# would be representative of the entire dataset

# To imagine that a dataset is a deck of cards

# Shuffling
# Each row is a different card

# The cards remain whole

# We don't lose any cards

# Shuffling
# Entire rows of data get moved up (or down) the dataset

# Their contents remain unchanged

# Data stored on the same row
# often refers to the same
# client or date

# For the initial part of this lecture,
# we'll use only the first 8 rows of the dataset

lending_co_data_numeric = np.genfromtxt("Lending-company-Numeric.csv", delimiter=',')[:8]
print(lending_co_data_numeric)

print(np.random.shuffle(lending_co_data_numeric))
# np.random.shuffle()
# Takes an ndarray and shuffles it in place

# It only saves the shuffled array over the original one

# No output

print(lending_co_data_numeric)

# Repeat

print(np.random.shuffle(lending_co_data_numeric))
print(lending_co_data_numeric)

# Can a dataset be shuffled only once?

# With each additional shuffle, the input dataset is the shuffled
# dataset from the previous time we shuffled

lending_co_data_numeric = np.loadtxt("Lending-company-Numeric.csv", delimiter=',')
print(lending_co_data_numeric)

# Whenever you're using the same function or method many times in your analysis,
# it's a good idea to directly import it

from numpy.random import shuffle

shuffle(lending_co_data_numeric)
print(lending_co_data_numeric)

# Random Generators:
# Generate Data
# Shuffling Data

from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg

array_RG = gen(pcg())
array_RG.shuffle(lending_co_data_numeric)
print(lending_co_data_numeric)

# Seeds fix random generators (in place) - Not True

# A shuffle prevails over the use of seeds

# We can't replicate the same shuffle twice