import pandas as pd
import numpy as np

prices_per_category = pd.Series({'Product A': 22250, 'Product B': 16600, 'Product C': 15600})
print(prices_per_category)

# print(prices_per_category.values)
print(prices_per_category.array) # recommended
# print(type(prices_per_category.values))
print(type(prices_per_category.array))

# pandas.array has been built on top of the numpy.array
# pandas.array extends the capabilities of the numpy.array

print(prices_per_category.to_numpy())
# This type of conversion allows you to proceed wih mathematical and statistical computations or further preprocessing of your data
print(type(prices_per_category.to_numpy()))
# This method has been introdduced to satisfy the increased demand for improved transformations of pandas Series into NumPy arrays

test_array = prices_per_category[['Product A', 'Product B']].to_numpy(dtype='float')
print(test_array)

print(type(test_array[0]))

print(prices_per_category.values[0])
print(type(prices_per_category.values[0]))

print(prices_per_category.array[0])
print(type(prices_per_category.array[0]))

print(prices_per_category.to_numpy()[0])
print(type(prices_per_category.to_numpy()[0]))