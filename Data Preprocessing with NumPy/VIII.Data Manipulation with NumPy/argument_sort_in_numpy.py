import numpy as np

# np.argsort()

lending_co_data_numeric = np.loadtxt("Lending-company-Numeric.csv", delimiter=",")
print(lending_co_data_numeric)

print(np.argsort(lending_co_data_numeric))

print(np.sort(lending_co_data_numeric))

print(np.sort(lending_co_data_numeric, axis=0))

print(np.argsort(lending_co_data_numeric, axis=0))

print(lending_co_data_numeric[482, 5])

print(np.argsort(lending_co_data_numeric[:, 0]))

lending_co_data_numeric = lending_co_data_numeric[np.argsort(lending_co_data_numeric[:, 0])]
# We refer to the code inse the square brackets as the "condition"

print(lending_co_data_numeric)

# This can be extremely useful when each row of a dataset
# contains information about a specific client (or date)

# ndarray.argsort() doesn't overwrite the original array

print(lending_co_data_numeric.argsort(axis=0))

print(lending_co_data_numeric)
# The method doesn't overwrite the original array

# np.argsort() = ndarray.argsort()
# np.sort() =/= ndarray.sort()

