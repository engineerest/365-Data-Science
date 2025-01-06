# Using Methods in Python - Part I

import pandas as pd

start_date_deposits = pd.Series({
    '7/4/2014' : 2000,
    '1/2/2015' : 2000,
    '7/8/2015' : 4500,
    '3/4/2015' : 6000,
    '4/5/2015' : 2000,
    '5/6/2015' : 1000,
    '6/7/2015' : 3000,

})

# Passive - Attributes - Metadata
# Active - Methods - Functionalities and behaviour of the object

# When provided with some initial data, both tools can make specific operations with it and return an output
# Functions:
# - an independent entity
# Methods:
# - can have access to the object's data
# - can manipulate the object's state
# pandas.Series

# Different libraries contain their own sets of methods

print(start_date_deposits)
print(start_date_deposits.sum) # return nothing
print(start_date_deposits.sum())
print(start_date_deposits.min())
# min() - returns the minimum of the values for the vertical axis
print(start_date_deposits.max())

# This isn't information about but it is information from our dataset

print(start_date_deposits.idxmax())
# idxmax() - returns the index label corresponding to the highest value in a series

print(start_date_deposits.idxmin())
# idxmin() - delivers the start date of the deposit with the smallest value

# You will be constantly using methods when working with Python or any of its related libraries and packages - Instructor

# Part II

# mathematical methods: .sum() .min() .max() .idxmin() .idxmax()
# numeric data only -> numpy
# both numeric and non-numeric data -> pandas

# Pandas won't deprive you of certain mathematical operations when you need them

print(start_date_deposits.head())
# The .head() method provides a quick and efficient way for you to catch a glimpse of the structure of your dataset
print(start_date_deposits.tail())


