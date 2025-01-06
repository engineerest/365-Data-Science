import pandas as pd

series_a = pd.Series([10, 20, 30, 40, 50])
print(series_a)

print(series_a.index)

print(type(series_a.index))
print(list(series_a.index))

prices_per_category = pd.Series({'Product A': 22250, 'Product B': 16600, 'Product C': 12500})
print(prices_per_category)

print(prices_per_category.index)
print(type(prices_per_category.index))