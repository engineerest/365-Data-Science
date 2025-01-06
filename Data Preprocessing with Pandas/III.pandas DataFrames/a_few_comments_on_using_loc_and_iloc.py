import pandas as pd

data = pd.read_csv('Lending-company.csv', index_col='LoanID')
lending_co_data = data.copy()
print(lending_co_data)

print(lending_co_data.shape)

# print(lending_co_data.iloc[1043, :]) error

# print(lending_co_data.iloc[:, 14]) error

print(lending_co_data.iloc[:, 13])

print(lending_co_data.iloc[:, -1])

# The Pythonic way means working with code that doesn't just use syntax correctly,
# but also lets us express our intentions clearly and explicitly

# Though most approaches you will see are valid examples of using Python correctly,
# only a few will be deemed Pythonic

print(lending_co_data.head())

# print(lending_co_data['TotalPrice'].iloc[0, :]) error

print(lending_co_data['TotalPrice'].iloc[0])

# print(lending_co_data['TotalPrice'][0])# error

# Since we have the index column explicitly,
# Python will automatically treat its values as labels

print(lending_co_data['TotalPrice'][1])

# print(lending_co_data['TotalPrice'].iloc[1]) error

# .iloc[] and .loc[] work predictably and are strictly used for integer - or label-location, respectively

data = pd.read_csv('Lending-company.csv', index_col='StringID')
lending_co_data = data.copy()
print(lending_co_data.head())

# print(lending_co_data['TotalPrice'].iloc[0])# error

print(lending_co_data['TotalPrice'].loc['LoanID_1'])

print(lending_co_data['TotalPrice'][0])

print(lending_co_data['TotalPrice'][1])

print(lending_co_data['TotalPrice']['LoanID_1'])

# You can trust the strict .loc[] and .loc[] indexers for position- and label-vased indexing

# print(lending_co_data[0][5]) error

# print(lending_co_data[0, 5]) error

# print(lending_co_data[[0, 5]]) error

# print(lending_co_data[[[0, 5]], :]) error

print(lending_co_data['TotalPrice']['LoanID_1'])

print(lending_co_data.loc['LoanID_1', 'TotalPrice'])

print(lending_co_data.loc[['LoanID_1', 'LoanID_6']])

print(lending_co_data.loc[['LoanID_1', 'LoanID_6'], :])

print(lending_co_data.TotalPrice['LoanID_1'])

# Choosing an explicit and clear technique for data selection is what ypu should be always aiming for

print(lending_co_data['TotalPrice'].iloc[[0, 5]])

# print(lending_co_data[:, 'TotalPrice'].iloc[[0, 5]]) error