import pandas as pd

data = pd.read_csv('Location.csv').squeeze(True)
location_data = data.copy()
print(location_data.head())

# In your analytic work, you will often need to apply several operations
# to your data until you can say that you have manipulated it in the desired way - Instructor

print(location_data.index)

# print(location_data.name) error

print(location_data.index.name)
location_data.index.name = 'Index'

print(location_data)

print(location_data.index.name)

print(location_data.sort_values())

print(location_data.sort_values().head())
print(location_data.sort_values().tail())

# Python allows you to logically focus on the object as well as what you want to obtain from it

print(location_data.index)
print(type(location_data.index))

print(location_data.index.to_numpy())

# Method chaining save you the time necessary for creating a variable and thinking of a relevant name