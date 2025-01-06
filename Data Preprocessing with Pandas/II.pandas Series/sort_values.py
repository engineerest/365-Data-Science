import pandas as pd

numbers = pd.Series([15, 1000, 23, 45, 444])
print(numbers)
# You'll sometimes need to order all rows from a data table not by its index,
# but according to the values of just one or a few of the columns

print(numbers.sort_values())

print(numbers.sort_values(ascending=True))
print(numbers.sort_values(ascending=False))

data = pd.read_csv('Location.csv').squeeze(True)
location_data = data.copy()
print(location_data.head())

print(location_data.sort_values())
print(location_data.sort_values(ascending=True))
print(location_data.sort_values(ascending=False))
# .sort_values() arranges the values of the object it's been applied to
# The index values comply with the object's data that will lead the way