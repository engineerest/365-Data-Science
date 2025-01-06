import numpy as np

# np.argwhere()

lending_co_data_numeric = np.loadtxt("Lending-company-Numeric.csv", delimiter=',')
print(lending_co_data_numeric)

print(np.argwhere(lending_co_data_numeric))
# The given result will make perfect sense in a few minutes

# np.argwhere()
# Goes over the entire NDarray and checks whether
# the individual elements satisfy a given condition

# The outputs are the indices for all
# the individual elements where the condition is met

# The default condition is to check for values different from 0

#   [[   0    0]
#   [   0    1]
#   [   0    2]
# 1.row  ...     2.column index
#   [1042    3]
#   [1042    4]
#   [1042    5]]

# The coordinates for each value from the original array
# (which satisfies the given condition)

print(np.argwhere(lending_co_data_numeric == False))

print(lending_co_data_numeric[116])

print(lending_co_data_numeric[430])

print(lending_co_data_numeric)

print(np.argwhere(lending_co_data_numeric % 2 == 0))
# % == remainder after division

# We can use this function to separate only the elements
# that interest us and examine just them

# Very similar to the "filtering"
# related to conditional slicing

# Slicing gives us the actual values

# np.argwhere() returns their
# coordinates within the array

# print(lending_co_data_numeric.argwhere()) error

# One of the ways np.argwhere()
# can be combined with another function

# np.isnan()      np.argwhere()

print(np.isnan(lending_co_data_numeric).sum())

lending_co_data_numeric_NAN = np.genfromtxt("Lending-company-Numeric-NAN.csv", delimiter=';')
print(lending_co_data_numeric_NAN)

print(np.isnan(lending_co_data_numeric_NAN))

print(np.argwhere(np.isnan(lending_co_data_numeric_NAN)))
# In Theory:
#               The coordinates for all
# False = 0 ->  the missing elements
#               of the array

print(lending_co_data_numeric_NAN[11])

print(lending_co_data_numeric_NAN[175])

# With the help of a single iteration we can fill all these values out

# We will use the structure of a very simple for loop

# ...
# [  85    4]
#  [ 117    5]
#  [ 152    1] The indices for individual elements
#  [ 152    2] that satisfy the condition we've set up
#  [ 152    4]
#  [ 172    1]
#  [ 175    1] Throughout every iteration,
#  [ 175    2] array_index contains the coordinates for a single point
# ...


for array_index in np.argwhere(np.isnan(lending_co_data_numeric_NAN)):
    lending_co_data_numeric_NAN[array_index[0], array_index[1]] = 0

print(lending_co_data_numeric_NAN[175])
# We've successfully found another way
# to take care of missing entries in the data

print(np.isnan(lending_co_data_numeric_NAN).sum())

# There are no longer missing values in this dataset
