import pandas as pd

products = ['A', 'B', 'C', 'D', 'E', 'F']
print(products)
print(type(products))

product_categories = pd.Series(products)
print(product_categories)
# object -  the default datatype assigned to data which is not numeric

print(type(product_categories))
print(type(pd.Series(products)))

daily_rates_dollars = pd.Series([40, 45, 50, 60])
print(daily_rates_dollars)

print(type(daily_rates_dollars))
# Pandas Series object corresponds to the one-dimensional NumPy array structure

import numpy as np

array_a = np.array([10, 20, 30, 40, 50])
print(array_a)
print(type(array_a))

series_a = pd.Series(array_a)
print(series_a)
print(type(series_a))

# Series => a larger set of tools and capabilities that are pertinent to the pandas library only

# The Series stores its values in a sequenced order, and has an explicit index

print(series_a.dtypes)
print(series_a.size)
# We can obtain information from all attributes related to the pandas "Series" class

product_categories = pd.Series(['A', 'B', 'C', 'D'])
print(product_categories)

print(product_categories.dtypes)
print(product_categories.size)

print(type(product_categories.size))
print(type(product_categories.name))
print(product_categories.name)

product_categories.name = "Product Categories"
print(product_categories)
print(product_categories.name)

# The attributes related to a certain Python object allow us
# to extract information about it but they are not meant
# to alter or modify its content in any way