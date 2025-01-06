import numpy as np

# Stacking

lending_co_data_numeric = np.loadtxt("Lending-company-Numeric.csv", delimiter=',')
print(lending_co_data_numeric)

# Recall

lending_co_data_numeric_NAN = np.genfromtxt("Lending-company-Numeric-NAN.csv", delimiter=';')

temporary_fill = np.nanmax(lending_co_data_numeric_NAN).round(2) + 1
temporary_mean = np.nanmean(lending_co_data_numeric_NAN, axis=0).round(2)

lending_co_data_numeric = np.genfromtxt("Lending-company-Numeric-NAN.csv",
                                        delimiter=';',
                                        filling_values=temporary_fill)

for i in range(lending_co_data_numeric_NAN.shape[1]):
    lending_co_data_numeric_NAN[:, i] = np.where(lending_co_data_numeric_NAN[:, i] == temporary_fill,
                                                 temporary_mean[i],
                                                 lending_co_data_numeric_NAN[:, i])

print(lending_co_data_numeric_NAN)

# Stacking:
# Placing multiple objects on top of one
# another to create a bigger (larger) object

# We can ust stack arrays of matching shapes
# to create a larger array - a "stack"

# np.stack()

print(np.stack((lending_co_data_numeric[:, 0], lending_co_data_numeric[:, 1])))

print(np.transpose(lending_co_data_numeric[:, :2]))

print(np.stack((lending_co_data_numeric[:, 1], lending_co_data_numeric[:, 0])))

# Stacking them on top of one another

# Stacking them side by side

# The axis determines how we stack these arrays

print(np.stack((lending_co_data_numeric[:, 0], lending_co_data_numeric[:, 1]), axis=1))

# We can stack multiple elements,
# rather than 2 at a time

print(np.stack((lending_co_data_numeric[:, 0], lending_co_data_numeric[:, 1], lending_co_data_numeric[:, 2]), axis=1))
# The arrays must be the same shape

# print(np.stack((lending_co_data_numeric[:, 0], lending_co_data_numeric[:, 1], lending_co_data_numeric[:, :2]), axis=1)) error
# ValueError: all input arrays must have the same shape

print(lending_co_data_numeric_NAN.shape)

# np.vstack()
# v stack = vertical stack
# The function stacks 2-D arrays vertically
# Places the first array on top of the second one
# Results in a "longer" array

print(np.vstack((lending_co_data_numeric, lending_co_data_numeric_NAN)))
print(np.vstack((lending_co_data_numeric, lending_co_data_numeric_NAN)).shape)

# np.hstack()
# h stack = horizontal stack
# Stacks values horizontally
# The result should be a "wider" array

print(np.hstack((lending_co_data_numeric, lending_co_data_numeric_NAN)))
# [[2.0000e+03 4.0000e+01 3.6500e+02 ... 3.1210e+03 4.2410e+03 1.3621e+04]
#  [2.0000e+03 4.0000e+01 3.6500e+02 ... 3.0610e+03 4.1710e+03 1.5041e+04]
#  [1.0000e+03 4.0000e+01 3.6500e+02 ... 2.1600e+03 3.2800e+03 1.5340e+04]
#  ... Contains more than 6 columns
#  [6.4002e+04 4.0000e+01 3.6500e+02 ... 4.2010e+03 5.0010e+03 1.6600e+04]
#  [1.0000e+03 4.0000e+01 3.6500e+02 ... 2.0800e+03 3.3200e+03 1.5600e+04]
#  [2.0000e+03 4.0000e+01 3.6500e+02 ... 4.6010e+03 4.6010e+03 1.6600e+04]]

print(np.hstack((lending_co_data_numeric, lending_co_data_numeric_NAN)).shape)

# np.dstack()
# A little different...
# d stack = depth stack
# We stack arrays in the third dimension
# Returns an array of a higher dimension

print(np.dstack((lending_co_data_numeric, lending_co_data_numeric_NAN)))
print(np.dstack((lending_co_data_numeric, lending_co_data_numeric_NAN)).shape)
# (1043, 6, 2) - 1043 6x2 arrays
# (1043, 6, 2) - (row, column, original array)

print(np.dstack((lending_co_data_numeric, lending_co_data_numeric_NAN))[0])
# [[ 2000.  2000.]
#  [   40.    40.]
#  [  365.   365.] Each column contains the first row
#  [ 3121.  3121.]
#  [ 4241.  4241.]
#  [13621. 13621.]]

print(np.dstack((lending_co_data_numeric, lending_co_data_numeric_NAN))[0, 0])
# [2000. 2000.]

# The second index must refer to the columns

print(np.dstack((lending_co_data_numeric, lending_co_data_numeric_NAN))[0, :, 0])
# We're slicing all the columns with a row index 0, and depth index 0
# The first row of the original dataset of variable

# When we're working with 2-D arrays, we can replicate its output with the np.stack() function.

print(np.stack((lending_co_data_numeric, lending_co_data_numeric_NAN), axis=-1))

# The stack function always returns an output that is exactly 1 dimension more than its inputs

# Since np.dstack() works along the "third" axis,
# the two function work indentically ( for 1-D and 2-D arrays)

array_example_1 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]],])
array_example_2 = array_example_1 * 2

print(np.dstack((array_example_1, array_example_2)))

print(np.stack((array_example_1, array_example_2), axis=-1).shape)

# The two functions are only ever equivalent for inputs of up to 2 dimensions