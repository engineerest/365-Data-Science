import numpy as np

# Removing values

lending_co_data_numeric = np.genfromtxt('Lending-company-Numeric.csv', delimiter=',')
print(lending_co_data_numeric)

print(np.delete(lending_co_data_numeric, 0))
print(np.delete(lending_co_data_numeric, 0).shape)
print(np.delete(lending_co_data_numeric, 0).size)

print(lending_co_data_numeric)

# What if we want to get rid of entire rows or columns?
# Pass a value to the axis argument

print(np.delete(lending_co_data_numeric, 0, axis=0))

print(np.delete(lending_co_data_numeric, 0, axis=1))

print(np.delete(lending_co_data_numeric, 1, axis=0))

print(np.delete(lending_co_data_numeric, (0, 2, 4), axis=0))

print(np.delete(lending_co_data_numeric, [0, 2, 4], axis=0))

print(np.delete(np.delete(lending_co_data_numeric, [0, 2, 4], axis=0), [0, 2, -1], axis=0))