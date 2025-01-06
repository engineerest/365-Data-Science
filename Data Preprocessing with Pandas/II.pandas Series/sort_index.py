import pandas as pd

data = pd.read_csv('Location.csv').squeeze(True)
location_data = data.copy()
print(location_data.head())

print(location_data.sort_values(ascending=False))

location_data_sv = location_data.sort_values(ascending=False)
print(location_data_sv.head())

print(location_data_sv.index)
print(location_data_sv.index.sort_values())
print(location_data_sv.head())

location_data_sv.index = location_data_sv.index.sort_values()
print(location_data_sv)

location_data_sv = location_data.sort_values(ascending=False)
print(location_data_sv.sort_index())
# .sort_index() creates a temporary copy of the object's data it's been applied to and displays the output of its manipulation
print(location_data_sv)

location_data_sv = location_data_sv.sort_index(ascending=True)
print(location_data_sv)

