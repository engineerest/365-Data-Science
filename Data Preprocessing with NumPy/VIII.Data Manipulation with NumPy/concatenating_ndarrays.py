import numpy as np

# Concatenate

lending_co_data_numeric = np.loadtxt("Lending-company-Numeric.csv", delimiter=',')
print(lending_co_data_numeric)

# Concatenating
# Linking together objects in a chain

# Creating a new (larger) array be merging existing smaller arrays along a given axis

# The inputs and the outputs of the np.concatenate() function always have the same
# number of dimensions

print(np.concatenate((lending_co_data_numeric[0, :], lending_co_data_numeric[1, :])))

# Recall:

lending_co_data_numeric_NAN = np.genfromtxt("Lending-company-Numeric-NAN.csv", delimiter=';')

temporary_fill = np.nanmax(lending_co_data_numeric_NAN).round(2) + 1
temporary_mean = np.nanmean(lending_co_data_numeric_NAN, axis=0).round(2)

lending_co_data_numeric_NAN = np.genfromtxt("Lending-company-Numeric-NAN.csv",
                                            delimiter=';',
                                            filling_values=temporary_fill)

for i in range(lending_co_data_numeric_NAN.shape[1]):
    lending_co_data_numeric_NAN[:, i] = np.where(lending_co_data_numeric_NAN[:, i] == temporary_fill,
                                                 temporary_mean[i],
                                                 lending_co_data_numeric_NAN[:, i])

print(lending_co_data_numeric_NAN)

print(np.concatenate((lending_co_data_numeric, lending_co_data_numeric_NAN)))

# We've concatenated the second dataset at the bottom of the first

print(np.concatenate((lending_co_data_numeric, lending_co_data_numeric_NAN)).shape)

print(np.concatenate((lending_co_data_numeric, lending_co_data_numeric_NAN), axis=1))

# The output consists of more than 6 columns

# We can assume the new array has 12 columns

print(np.concatenate((lending_co_data_numeric, lending_co_data_numeric_NAN), axis=1).shape)

# print(np.concatenate((lending_co_data_numeric, lending_co_data_numeric_NAN), axis=2)) error
# numpy.exceptions.AxisError: axis 2 is out of bounds for array of dimension 2


array_example_1 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]],])
array_example_2 = array_example_1 * 2

print(np.concatenate((array_example_1, array_example_2), axis=0))

print(np.concatenate((array_example_1, array_example_2), axis=1))

print(np.hstack((array_example_1, array_example_2)))

# np.concatenate() can replicate the outputs of these 3 stacking functions

# np.concatenate() works exactly like np.hstack(), np.vstack() and np.dstack()
# depending on the inputs, and axis arguments
# 1 % 2 - D arrays:
# np.hstack() -> np.concatenate((), axis=0)
# np.vstack() -> np.concatenate((), axis=1)
# np.dstask() -> np.concatenate((), axis=2)

# Concatenating inputs of different shapes

print(np.concatenate((lending_co_data_numeric[0, :], lending_co_data_numeric[:, 0])))

# Concatenating in 1-D does not require the inputs to have the same shape

# print(np.concatenate((lending_co_data_numeric, lending_co_data_numeric[:, 0]))) error
# ValueError: all the input arrays must have same number of dimensions,
# but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)

# However if we have arrays of the same dimensions, but different shapes, we can still
# concatenate them. But only if their dimensions match for the axis we're concatenating along.

# If we remove a row, we can still concatenate vertically
print(np.concatenate((lending_co_data_numeric, lending_co_data_numeric[1:, :])))

# print(np.concatenate((lending_co_data_numeric, lending_co_data_numeric[:, :1]))) error
# ValueError: all the input array dimensions except for the concatenation axis must match exactly,
# but along dimension 1, the array at index 0 has size 6 and the array at index 1 has size 1