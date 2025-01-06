import pandas as pd

data = pd.read_csv('Lending-company.csv', index_col='StringID')
lending_co_data = data.copy()
print(lending_co_data.head())

# print(lending_co_data[1]) error
# Position 1 -> lending_co_data['Product']

print(lending_co_data['Product'])

print(lending_co_data.iloc[1])
print(lending_co_data.iloc[1, 3])

# .iloc[] has been programmed to deliver the desired portion of the dataset whether we provide one or two location specifiers

print(lending_co_data.iloc[1, :]) # data from all columns
print(lending_co_data.iloc[:, 3])

print(type(lending_co_data.iloc[1, 3]))
print(type(lending_co_data.iloc[1, :]))
print(type(lending_co_data.iloc[:, 3]))

print(lending_co_data.iloc[[1, 3], :])
print(lending_co_data.iloc[:, [3, 1]])