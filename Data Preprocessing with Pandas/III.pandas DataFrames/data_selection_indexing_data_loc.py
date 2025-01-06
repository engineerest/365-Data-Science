import pandas as pd

data = pd.read_csv('Lending-company.csv', index_col='StringID')
lending_co_data = data.copy()
print(lending_co_data)

print(lending_co_data.loc['LoanID_3'])

print('\n\n\n', lending_co_data.loc['LoanID_3', :])

print('\n\n\n', lending_co_data.loc['LoanID_3', 'Region'])

# print('\n\n\n', lending_co_data.loc['Location']) error

print('\n\n\n', lending_co_data.loc[:, 'Location'])

# print('\n\n\n', lending_co_data.loc[:, 'Locations']) error
