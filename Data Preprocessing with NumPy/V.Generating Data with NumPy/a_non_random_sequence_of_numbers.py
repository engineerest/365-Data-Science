import numpy as np

# np.arange()

# arange = array range
# NumPy's equivalent of Python's range function

# Creates a sequence of consecutive integer values within a given range

# range -> range object
# array range -> array

print(list(range(30)))

array_rng = np.arange(30)
print(array_rng)

# Closed-open means we include the lower bound, but not the upper one

array_rng = np.arange(stop=30) # error in course, but actually not
# array_rng = np.arange(start=30) actually error
print(array_rng)

array_rng = np.arange(start=0, stop=30)
print(array_rng)

array_rng = np.arange(start=0, stop=30, step=2.5)
print(array_rng)

array_rng = np.arange(start=0, stop=30, step=2.5, dtype=np.int32)
print(array_rng) # This function work solely within the realm of integers


