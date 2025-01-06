import numpy as np

# Casting

lending_co_data_numeric = np.loadtxt('Lending-company-Numeric.csv', delimiter=',')
print(lending_co_data_numeric)

# Type Casting (Casting):
# Taking an object with values of a certain datatype and creating
# an identical object that contains values of a different datatype.

# Creating a new array that stores the values
# of the original array under a different type

# decimals -> integers
# or vice versa
# decimals <- integers

print(lending_co_data_numeric.astype(dtype=np.int32))
# astype = assign type
# dtype = datatype
# np.int32 = integer values (up to 32 bits)

# [[ 2000    40   365  3121  4241 13621]
#  [ 2000    40   365  3061  4171 15041]
#  [ 1000    40   365  2160  3280 15340]
#  ...
#  [ 2000    40   365  4201  5001 16600]
#  [ 1000    40   365  2080  3320 15600]
#  [ 2000    40   365  4601  4601 16600]]
# No decimal points in the obtained values

# floats -> integers - it is easy

# strings(limited operations) -> integers


print(lending_co_data_numeric.astype(dtype=np.str_))
# str = string
# Doesn't overwrite the array in place

lending_co_data_numeric = lending_co_data_numeric.astype(dtype=np.str_)
print(lending_co_data_numeric)
# All the elements look like floats,
# but have quotation marks around them

print(type(lending_co_data_numeric))

# The dataset retains all of its functionalities

# print(lending_co_data_numeric.astype(dtype=np.int32)) error
# ValueError: invalid literal for int() with base 10: np.str_('2000.0')
# . - Not an element recognized among integers

# We can't directly cast these string into integers
# strings -> integers
# but
# strings -> floats -> integers

print(lending_co_data_numeric.astype(dtype=np.float32))

lending_co_data_numeric = np.loadtxt('Lending-company-Numeric.csv', delimiter=',')
print(lending_co_data_numeric.astype(dtype=np.str_))
print(lending_co_data_numeric)

print(lending_co_data_numeric.astype(dtype=np.float32).astype(dtype=np.int32))
print(lending_co_data_numeric)