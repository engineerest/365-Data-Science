import numpy as np

lending_co_lt = np.genfromtxt('lending-co-LT.csv', delimiter=',')
# More stable than np.loadtxt()
# All columns from LoanID to TotalPrice
print(lending_co_lt)
# We have different ways of displaying these datasets

# Either approach (directly calling te variable vs print()) is equally appropriate

# 1.041e+03 = %e+03 - Scientific notation
# nan = not a number
# 1.660e+04 = 1.660*10^(4) = 1.660 * 10,000 = 16,600

# The dafault input assumes decimal numbers for the entire dataset

lending_co_lt = np.genfromtxt('lending-co-LT.csv', delimiter=',', dtype=np.int32)
# np.int32
# np -> NumPy-specific datatype
# int32 -> Integers up to 32 bits
print(lending_co_lt)

# By specifying the input data to be of a specific type,
# the function generates the missing values differently

print(lending_co_lt[0, 0] + lending_co_lt[0, 1])

lending_co_lt = np.genfromtxt('lending-co-LT.csv', delimiter=',', dtype=np.int_)
# np.str_ = NumPy strings
# Import the entire dataset as text
print(lending_co_lt)

# The values within the quotation marks are literally the symbols stored in the variable

# We cannot add the values up or ddo other mathematical operations

# The different elements within the array can still be sorted, cut and formatted

lending_co_lt = np.genfromtxt('lending-co-LT.csv', delimiter=',', dtype=np.object_)
print(lending_co_lt)
# The data inside is not just plain text we can't freely manipulate the values
# Better compatibility with older versions of the Pandas package
# Series no longer store strings as objects

# The number of datatypes is determined by the number of columns or fields in the dataset