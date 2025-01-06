import pandas as pd
import numpy as np

data = pd.read_csv('Lending-company.csv', index_col='LoanID')
lending_co_data = data.copy()
print(lending_co_data.head())

print(lending_co_data.index)
print(type(lending_co_data.index))

print(lending_co_data.columns)
print(type(lending_co_data.columns))

print(lending_co_data.axes)

print(lending_co_data.dtypes) # data types

print(lending_co_data.values)
print(type(lending_co_data.values))

print(lending_co_data.to_numpy())
print(type(lending_co_data.to_numpy()))

print(lending_co_data.shape)

print(len(lending_co_data.columns))
