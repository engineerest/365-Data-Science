import pandas as pd

# Creating DataFrames from Scratch

# Construct a DataFrame from a dictionary of lists

data = {'ProductName': ['Product A', 'Product B', 'Product C'], 'ProductPrice':[22250, 16600, 12500]}
df = pd.DataFrame(data)
print(df)

# Construct a DataFrame from a dictionary of lists + specify an index

df = pd.DataFrame(data, index=['A', 'B', 'C'])
print(df)

product_IDs = ['A', 'B', 'C']
df = pd.DataFrame(data, index=product_IDs)
print(df)

# Construct a DataFrame from a list of dictionaries

data = [
    {
        'ProductName':'Product A', 'ProductPrice': 22250
    },
    {
        'ProductName':'Product B', 'ProductPrice': 16600
    },
    {
        'ProductName':'Product C', 'ProductPrice': 12500
    }
]

df = pd.DataFrame(data)
print(df)

data = [
    {
        'ProductName':'Product A', 'ProductPrice': 22250
    },
    {
        'ProductName':'Product B', 'ProductPrice': 16600
    },
    {
        'ProductName':'Product C', 'ProductPrice': [12500, 100000]
    }
]
df = pd.DataFrame(data)
print(df)

data = [
    {
        'ProductName':'Product A', 'ProductPrice': 22250
    },
    {
        'ProductName':'Product B', 'ProductPrice': 16600
    },
    {
        'ProductName':'Product C', 'ProductPrice': [12500, 100000]
    },
    {
        'ProductName':'Product D'
    }
]
df = pd.DataFrame(data)
print(df)

# Construct a DataFrame form a dictionary of pandas Series

ser_products = pd.Series(['Product A', 'Product B', 'Product C'])
ser_prices = pd.Series([22250, 16600, 12500])

data = {'ProductName': ser_products, 'ProductPrice': ser_prices}
df = pd.DataFrame(data)

ser_products = pd.Series(['Product A', 'Product B', 'Product C'], index=['A', 'B', 'C'])
ser_prices = pd.Series([22250, 16600, 12500], index=['A', 'B', 'C'])

data = {'ProductName': ser_products, 'ProductPrice': ser_prices}
df = pd.DataFrame(data)
print(df)

ser_prices = pd.Series([22250, 16600, 12500], index=['C', 'B', 'A'])
data = {'ProductName': ser_products, 'ProductPrice': ser_prices}
df = pd.DataFrame(data)
print(df)

# If you change the order of the index of one of the series,
# Python will eventually match its elements with their corresponding indices

# In the final output, it will re-organise the values of every row to respond to the order provided in the index of the first series

# Construct a DataFrame from a list to lists

# The number of elements in each inner list must be fixed

data = [['Product A', 22250], ['Product B', 16600], ['Product C', 12500]]
df = pd.DataFrame(data)
print(df)

data = [['Product A', 22250], ['Product B', 16600], ['Product C', 12500, 5000]]
df = pd.DataFrame(data)
print(df)

data = [['Product A', 22250], ['Product B', 16600], ['Product C', 12500]]
df = pd.DataFrame(data)
print(df)

df.columns = ['ProductName', 'ProductPrice']
print(df)

df.index = ['A', 'B', 'C']

# Construct a DataFrame in a Professional Way

df = pd.DataFrame(
    data=[['Product A', 22250], ['Product B', 16600], ['Product C', 12500]],
    columns=['ProductName', 'ProductPrice'],
    index=['A', 'B', 'C']
)
print(df)

print(df.shape)
# .shape - provides the number of rows and columns you currently have in your DataFrame

# There are plenty of other ways to obtain the same results