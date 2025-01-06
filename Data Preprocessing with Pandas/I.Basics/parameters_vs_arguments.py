import pandas as pd

from using_methods import start_date_deposits

# One of the best features of using methods is that we can also modify their performance

print(start_date_deposits.head())
print(start_date_deposits.head(3))
print(start_date_deposits.head(10))
print(start_date_deposits.head())
# The .head() method provides us with the option to choose the number of displayed rows from the object it has been applied

# .head(10) - an argument (our choice for n)
# .head() - a parameter (n)

# start_date_deposit.head(5) = start_date_deposit.head()

# A parameter of a Python method or function always has a name

print(start_date_deposits.head(n=10))

# What parameters you're providing the arguments for

# Pandas methods have parameters you can supply with arguments to modify the performance of the given method

# It is good practice to refer to the parameters by using their names explicitly an in the right order