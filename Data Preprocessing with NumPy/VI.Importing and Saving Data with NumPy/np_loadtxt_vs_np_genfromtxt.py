import numpy as np

# np.loadtxt vs np.genfromtxt()

# Both functions are part of the NumPy package

# "load" implies the data is ready to be directly imported and used

# "generate" indicates that the function creates the data set from the text file

# Generating requires constructing the array as we go through the text file

# np.loadtxt() - faster
# np.genfromtxt() - has more flexibility

lending_co_data_numeric_1 = np.loadtxt("Lending-Company-Numeric-Data.csv", delimiter=',')
# Faster of the two, but it breaks whe we feed it incomplete or ill-formatted datasets

# These are our own naming conventions and you can name your variable whatever you like

# File Name:
# Typically stored in the same directory (folder) as your Python notebook (code file)

# If not, you'd have to specify the entire path leading to the file you want to import

# \n, \t

# Delimiters
# Pre-defined symbols (e.g."," and ";") which are use to define distinct fields in text files (e.g. cells in a row, rows in a table)

# A very common approach is to store large datasets in text files this way (text separated by delimiters)

# Big and import datasets come with a brief summary explaining these specifics

print(lending_co_data_numeric_1)
# More rows with data between the first 3 and the last 3

lending_co_data_numeric_2 = np.genfromtxt("Lending-Company-Numeric-Data.csv", delimiter=',')
#
print(lending_co_data_numeric_2)

print(np.array_equal(lending_co_data_numeric_1, lending_co_data_numeric_2))

# Lending-Company-Numeric-Data-NAN.csv
# NAN

# NAN = Not A Number

# Refers to missing values within a NumPy array

# lending_co_data_numeric_NAN = np.loadtxt("Lending-Company-Numeric-Data-NAN.csv", delimiter=';') error
# print(lending_co_data_numeric_NAN)

# Python encounters a symbol when it expects a number

# Missing Values = ""(empty space)

# "" (empty space) counts as a symbol

lending_co_data_numeric_NAN = np.genfromtxt("Lending-Company-Numeric-Data-NAN.csv", delimiter=';') # Handles missing data well
print(lending_co_data_numeric_NAN)

lending_co_data_numeric_NAN = np.loadtxt("Lending-Company-Numeric-Data-NAN.csv", delimiter=';', dtype=np.str_)
print(lending_co_data_numeric_NAN)

# They are saved as plain ext rather than numbers

# All the values now have single quotes around them (e.g. '2000')

print(lending_co_data_numeric_NAN[0, 0] + lending_co_data_numeric_NAN[0, 1])

# We can use the second way of importing this dataset only if we want observe the data values that have been stored in it,
# and we DON'T  need to execute any mathematical operations