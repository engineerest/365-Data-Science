import pandas as pd

data = pd.read_csv('Lending-company.csv', index_col='StringID')
lending_co_data = data.copy()
print(lending_co_data.head())

print(lending_co_data.Product)
print(lending_co_data.Location)

print(lending_co_data['Product'])
print(lending_co_data['Location'])
# print(lending_co_data['location']) error, it isn't exist

print(type(lending_co_data['Location']))

print(lending_co_data[['Location']])
print(type(lending_co_data[['Location']]))

print(lending_co_data[['Location', 'Product']].head())

prod_loc = ['Location', 'Product']
print(lending_co_data[prod_loc].head())

# print(lending_co_data['Product', 'Location']) error
