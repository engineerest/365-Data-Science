import pandas as pd

prices_per_category = {"Product A": 22250, 'Product B': 16600, 'Product C': 15600}
print(prices_per_category)
print(type(prices_per_category))

prices_per_category = pd.Series(prices_per_category)
print(prices_per_category)
print(type(prices_per_category))

print(prices_per_category.index)
print(type(prices_per_category.index))