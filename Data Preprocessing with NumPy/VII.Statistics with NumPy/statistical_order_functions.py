import numpy as np

matrix_a = np.array([[1, 0, 0, 3, 1], [3, 6, 6, 2, 9], [4, 5, 3, 8, 0]])
print(matrix_a)

# np.ptp()
# ptp = peak to peak
# Returns the difference between the highest and lowest values within an array

print(np.ptp(matrix_a))
# [[1 0 0 3 1]
#  [3 6 6 2 9] <- np.max()
#  [4 5 3 8 0]] <- np.min()

# Convenient and time-saving to use one functions instead two

print(np.ptp(matrix_a, axis=0)) # 4-1, 6-0, 6-0, 8-2, 9-0
print(np.ptp(matrix_a, axis=1)) # 3-0, 9-2, 8-0

# np.percentile()
# Returns a specific percentile of a given set
# Requires a second input - the percentile

# percentile
# A value that is greater that the corresponding % of the dataset
# The The 70-th percentile is greater that 70% of the data
# We're 70% through a sorted version of the array (in increasing order)

print(np.sort(matrix_a, axis=None)) # 4, 5

print(np.percentile(matrix_a, 70)) # 4,79(9) linear interpolation
# 15 * 0.7 = 10.5

print(np.percentile(matrix_a, 70, interpolation="midpoint"))

print(np.percentile(matrix_a, 70, interpolation="lower"))

print(np.percentile(matrix_a, 70, interpolation="nearest"))

print(type(np.percentile(matrix_a, 70, interpolation="nearest")))

print(type(np.percentile(matrix_a, 70)))

# We need to keep track of what interpolation we set when computing the percentile

print(np.percentile(matrix_a, 50))
# median = middle value of a sorted dataset

print(np.percentile(matrix_a, 100))

# quantile:
# A value that is greater that the corresponding part of the dataset
# 70-th percentile = 0.7 quantile

print(np.quantile(matrix_a, 0.70))

print(np.quantile(matrix_a, 0.70, interpolation="nearest"))

print(np.quantile(matrix_a, 0.70, method="nearest"))
# However, in our days, the interpolation was called a method in numpy, so use the method instead interpolation