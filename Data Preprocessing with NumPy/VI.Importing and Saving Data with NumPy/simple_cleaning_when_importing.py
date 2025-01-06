import numpy as np

lending_co_data_numeric_NAN = np.genfromtxt('Lending-Company-Numeric-Data-NAN.csv', delimiter=';')
print(lending_co_data_numeric_NAN)

# Beneficial when we're familiar with our data

lending_co_data_numeric_NAN = np.genfromtxt('Lending-Company-Numeric-Data-NAN.csv',
                                            delimiter=';',
                                            skip_header=2)

# skip_header
# "skip_header = 2" should remove the first 2 lines of the dataset
# Becomes convenient when text files include several lines of comments and notes from the authors
# We can omit as many lines as we want from the top of the dataset
print(lending_co_data_numeric_NAN)

# skip_header works as intended

lending_co_data_numeric_NAN = np.genfromtxt('Lending-Company-Numeric-Data-NAN.csv',
                                            delimiter=';',
                                            skip_footer=2)
print(lending_co_data_numeric_NAN)

# skip_footer
# "skip_footer = 2" will disregard the last two lines of the dataset when importing it
# skip_footer behaves as expected, too

# usecols

lending_co_data_numeric_NAN = np.genfromtxt('Lending-Company-Numeric-Data-NAN.csv',
                                            delimiter=';',
                                            usecols=(0, 1, 5))

# "usecols = 0" will tell Python we're only interested in the first column

# put all the values in parentheses (a tuple)

# Python uses 0-indexing

# We don't have to import these columns in order (the order they appear in)

# 1st, 2nd and 6-th columns

print(lending_co_data_numeric_NAN)

lending_co_data_numeric_NAN = np.genfromtxt('Lending-Company-Numeric-Data-NAN.csv',
                                            delimiter=';',
                                            usecols=(5, 0, 1))

print(lending_co_data_numeric_NAN)

# This technique can be extremely convenient when we want to sort the data
# according to a given metric which isn't stored in the fartest column to the left (index 0)

# We can use these arguments simultaneously

lending_co_data_numeric_NAN = np.genfromtxt('Lending-Company-Numeric-Data-NAN.csv',
                                            delimiter=';',
                                            usecols=(0, 1, 5),
                                            skip_header=2,
                                            skip_footer=2)
print(lending_co_data_numeric_NAN)

# lending_co_data_numeric_5, lending_co_data_numeric_0, lending_co_data_numeric_1 = np.genfromtxt('Lending-Company-Numeric-Data-NAN.csv',
#                                                                                                 delimiter=';',
#                                                                                                 usecols=(5, 0, 1),
#                                                                                                 skip_header=2,
#                                                                                                 skip_footer=2) error

# Trying to pass a single value to 3 variables

# Split (or upack) the output in (in this case 3) different streams

lending_co_data_numeric_5, lending_co_data_numeric_0, lending_co_data_numeric_1 = np.genfromtxt('Lending-Company-Numeric-Data-NAN.csv',
                                                                                                delimiter=';',
                                                                                                usecols=(5, 0, 1), # It's important to remember that
                                                                                                # the output is generated (and then unpacked) according to order
                                                                                                # in the usecols argument
                                                                                                skip_header=2,
                                                                                                skip_footer=2,
                                                                                                unpack=True)

print(lending_co_data_numeric_5)
print(lending_co_data_numeric_0)
print(lending_co_data_numeric_1)