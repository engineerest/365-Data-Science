# Defining Random Generators

from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg

# The Generator function takes a bit generator as an input and creates generator objects

# numpy.random.Generator class
# PCG - Permutation Congruential Generator

# FUnction pointers that can produce values of up to 64 bits in size

array_RG = gen(pcg())# specify a seed for the Generator object
print(array_RG.normal())

print(array_RG.normal(size=5))

print(array_RG.normal(size=(5, 5)))
# Clarification: The shape of the array will be equal to the tuple ((5, 5) in this case)

# Every time we call a method, the Generator randomly selects a "seed"
# Seed - a set of starting parameters for the algorithm

# Random Dataset -> Model

array_th = gen(pcg(seed=365))
# Using 365 will ensure your outputs match ours
print(array_RG.normal(size=(5, 5)))

print(array_RG.normal(size=(5, 5))) # A seed only lasts for one execution of a method or function before it is reset

# Generating Integers, Probabilities and Random Choices

# Seed reset after every execution

array_RG = gen(pcg(seed=365))

# numpy.integers()

# Generates whole numbers (integers)
# Requires defining a fixed range of values to s=choose from
# If we only provide a single value it automatically assumes we only want integers between 0 and it

print(array_RG.integers(10, size=(5, 5)))

print(array_RG.integers(low=10, size=(5, 5)))

print(array_RG.integers(low=10, high=100, size=(5, 5)))

print(array_RG.random(size=(5, 5)))

# numpy.choice

# Simulates the idea of making an arbitrary choice out of a given sequence

print(array_RG.choice([1, 2, 3, 4, 5], size=(5, 5))) # All the outcomes are equally likely

# print(array_RG.choice([1, 2, 3, 4, 5], p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.7], size=(5, 5))) error
# print(array_RG.choice([1, 2, 3, 4, 5], p=[0.1, 0.1, 0.1, 0.1, 0.7], size=(5, 5))) error
# the probabilities sums must be 1
print(array_RG.choice([1, 2, 3, 4, 5], p=[0.1, 0.1, 0.1, 0.1, 0.6], size=(5, 5)))
