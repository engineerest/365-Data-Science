import pandas as pd

series_a = pd.Series([10, 20, 30, 40, 50])
prices_per_category = pd.Series({'Product A': 22250, 'Product B': 16600, 'Product C': 12500})

print(series_a)
print(series_a[0])
print(prices_per_category)
print(prices_per_category['Product A'])
print(prices_per_category[0])

series_b = pd.Series([10, 20, 30, 40, 50], index=[1, 2, 3, 4, 5])
print(series_b)

# print(series_b[0]) error
print(series_b[1])

series_c = pd.Series([10, 20, 30, 40, 50], index=["1", "2", "3", "4", "5"])
print(series_c)

print(series_c[1])
print(series_c["1"])
print(series_c[0])
print(prices_per_category)