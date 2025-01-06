import numpy as np

# Sorting Data

lending_co_data_numeric = np.loadtxt('Lending-company-Numeric.csv', delimiter=',')
print(lending_co_data_numeric)

# np.sort()
# Takes an array and returns a sorted version
# (in ascending order)

print(np.sort(lending_co_data_numeric))
# The "default" sort
# Run the function without specifying any other argument

# Default axis=-1
# axis -1 = the "last" axis
# lending_co_data_numeric has on;y 2 axes -> 0 and 1

# the "second" axis = axis with index 1 is also the "last" axis the column axis
# We're rearranging the different columns in every row

# An array where all the rows are sorted

print(np.sort(lending_co_data_numeric).shape)
print(lending_co_data_numeric.shape)

print(np.sort(lending_co_data_numeric, axis=0))

# We cant tell NumPy to refrain from using scientific notation

print(np.set_printoptions(suppress=True))
# These setting will apply to our entire work


print(np.sort(lending_co_data_numeric, axis=None))
# Informs the function to work with the flatted version of the 2-D input

# The flattened array is 1-D, then so is its sorted version

# NumPy's sort function doesn't have a parameter
# that automatically changes the order from increasing to decreasing

print(np.sort(lending_co_data_numeric))

print(np.sort(-lending_co_data_numeric))
# "-" literally changes the sign of every individual element of the input variable
# Equivalent to multiplying by -1

# The matrix we see on screen isn't the original array sorted in decreasing order

print(-np.sort(-lending_co_data_numeric))

# We've successfully sorted each line of the initial matrix in descending order

print(lending_co_data_numeric)

print(np.sort(lending_co_data_numeric[:, 3]))

# The sort function returns a sorted version the original array, rather than sorting it in place

# print(np.sort(lending_co_data_numeric[:, 3].sort())) error
print(np.sort(lending_co_data_numeric).sort(axis=0))
print(lending_co_data_numeric)
