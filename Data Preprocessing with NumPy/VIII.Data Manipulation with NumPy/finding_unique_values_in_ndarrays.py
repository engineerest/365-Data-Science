import numpy as np

# Unique
lending_co_data_numeric = np.loadtxt("Lending-company-Numeric.csv",
                                     delimiter=",")
print(lending_co_data_numeric)

# np.unique()
# Takes an array as an input and creates another array that contains all the different
# values from the first one

# Any value can feature only once in the np.unique() output

print(np.unique(lending_co_data_numeric))

print(np.unique(lending_co_data_numeric[:, 1]))
# Arranged in "increasing" fashion

array_example = np.array(["a1", "a3", "A1", "A1", "A3", "A3", "AA1", "B1", "A2", "B1", "A2", "B2", "B2", "B3", "a2", "a3", "B3", "B3", "a3"])
print(np.unique(array_example))
# Arranged in alphabetic order

# Arrange based on their ASCII values

# A < a
# A < B, a < b
# 3 < A

print(np.unique(lending_co_data_numeric[:, 1], return_counts=True))

# Meaningful information for statistical analysis

print(np.unique(lending_co_data_numeric[:, 1], return_counts=True, return_index=True))

# The array with 0 is the index array