# THe pandas Series object represents a single-column ddata or a set of observations related to a single variable

# One-dimensional NumPy array structure

import pandas as pd

data = pd.read_csv('Location.csv').squeeze(True)
location_data = data.copy()
print(location_data.head())

# The idea: Back up your data cleaning and data manipulation skills with analytical intuition

print(type(location_data))
print(location_data.describe())
print(len(location_data))

print(location_data.nunique())
print(type(location_data.nunique()))

# print(location_data.unique()) error
# print(type(location_data.unique())) error

