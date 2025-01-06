import pandas as pd
import numpy as np

# DataFrame - a tabular structure that contains multiple observations for a given set of variables

# Two-dimensional -> Two points of reference: 1.The column of interest; 2.The relevant row.

# DataFrame - a collection of one or several Series objects

# Every column from the DataFrame is a Series object itself

# The information in the DataFrame can potentially be heterogeneous

array_a = np.array([[3, 2, 1], [6, 3, 2]])
print(array_a)

print(pd.DataFrame(array_a))
print(type(pd.DataFrame(array_a)))

df = pd.DataFrame(array_a, columns=['Column1', 'Column2', 'Column 3'])
print(df)

df = pd.DataFrame(array_a, columns=['Column1', 'Column2', 'Column 3'], index=['Row1', 'Row2'])

data = pd.read_csv('Lending-company.csv', index_col='LoanID')
lending_co_data = data.copy()
print(lending_co_data.head())

print(type(lending_co_data))