import numpy as np

matrix_a = np.array([[1, 0, 0, 3, 1], [3, 6, 6, 2, 9], [4, 5, 3, 8, 0]])
print(matrix_a)

# np.median()
# Takes an input array and returns its median value
# median - The middle value of a sorted dataset
# If there are an even number of elements,
# it's the average of the two middle ones

print(np.median(matrix_a))

print(np.sort(matrix_a, axis=0))

# We only care about the 8th element,
# but all 3 being equal makes it easy to
# determine the median at a glance

# np.mean()
# Calculates the arithmetic average of all the values in the dataset

print(np.mean(matrix_a))

# np.average()
# Computes the average (of an array)

print(np.average(matrix_a)) # Can compute the weighted average of a dataset

# We can set these values (weights) manually, or...
# ...we can use a Random Generator...

from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg

array_RG = gen(pcg(seed=(365)))

array_weights = array_RG.random(size=(3, 5))
print(array_weights)

print(np.average(matrix_a, weights=array_weights))
# We've assigned weights to each element

# np.var()
# var - short for "variance"
# Only requires a single input

print(np.var(matrix_a))

# We don't want to spend more time testing the accuracy of functions that have been staples of NumPy for years

# np.std()
# std - stands for "standard deviation"

print(np.std(matrix_a))

# Variance = Standard Deviation^2

print(2.8**2)

