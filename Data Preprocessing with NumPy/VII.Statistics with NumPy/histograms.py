import numpy as np

matrix_a = np.array([[1, 0, 0, 3, 1], [3, 6, 6, 2, 9], [4, 5, 3, 8, 0]])
print(matrix_a)

# Histogram:
# A way to examine a dataset by dissecting
# How populate a given area is
# How many values from a dataset fall within some predetermined range
# How many values of the original dataset fall within each interval

print(np.sort(matrix_a, axis=None))

print(np.histogram(matrix_a))
# (array([3, 2, 1, 3, 1, 1, 2, 0, 1, 1]), <- 10
# array([0. , 0.9, 1.8, 2.7, 3.6, 4.5, 5.4, 6.3, 7.2, 8.1, 9. ])) <- 11

# 1 is the only integer in the range [0.9, 1.8]

print(np.histogram(matrix_a)[0])
print(np.histogram(matrix_a)[1])
# Bins are closed-open intervals [a, b]

# If a value equals the lower edge of a bin,
# it counts towards the bin

# If it equals the upper edge, it doesn't

# bing default is 10

print(np.histogram(matrix_a, bins=4))

# The fewer bins, the further away the edges are

# Fewer bins leads to a higher average number of elements in each bin

# range
# defining a fixe interval
# very easy way to ignore outliers

print(np.histogram(matrix_a, bins=4, range=(1, 7)))

# A fixed range implies a maximal an minimal value which are incorporated for the bins


import matplotlib.pyplot as plt
plt.hist(matrix_a.flat, bins=np.histogram(matrix_a)[1])
plt.show()

# 2-D Histograms
# X [[9 75 60 ... 8 54 17]
# Y [79 58 54 ... 82 14 94]]
# How the values are spread out across the plain

print(matrix_a)
# [[1 0 0 3 1] X
#  [3 6 6 2 9] Y
#  [4 5 3 8 0]]
print(np.histogram2d(matrix_a[0], matrix_a[1], bins=4))
# (array([[0., 0., 2., 0.],
#        [1., 0., 0., 1.],
#        [0., 0., 0., 0.],
#        [1., 0., 0., 0.]]), - density array

#        array([0.  , 0.75, 1.5 , 2.25, 3.  ]), - bin edges
#        array([2.  , 3.75, 5.5 , 7.25, 9.  ])) - bin edges

# First row = All points whose X-value falls within the first bin

# row -> X bin
# column -> Y bin

print(np.histogramdd(matrix_a.transpose(), bins=4))

# (array([[[0., 0., 0., 0.],
#         [0., 0., 0., 0.],
#         [0., 1., 1., 0.],
#         [0., 0., 0., 0.]],
#
#        [[0., 0., 1., 0.],
#         [0., 0., 0., 0.],
#         [0., 0., 0., 0.],
#         [1., 0., 0., 0.]],
#                           # All of these, 2-D density array for each bin of the Z-coordinate array

                            # density tensor (depicts the density in 3 dimensions)
#        [[0., 0., 0., 0.],
#         [0., 0., 0., 0.],
#         [0., 0., 0., 0.],
#         [0., 0., 0., 0.]],
#
#        [[0., 0., 0., 1.],
#         [0., 0., 0., 0.],
#         [0., 0., 0., 0.],
#         [0., 0., 0., 0.]]]),

# One for each array of the input matrix

#         [array([0.  , 0.75, 1.5 , 2.25, 3.  ]),
#         array([2.  , 3.75, 5.5 , 7.25, 9.  ]),
#         array([0., 2., 4., 6., 8.])])