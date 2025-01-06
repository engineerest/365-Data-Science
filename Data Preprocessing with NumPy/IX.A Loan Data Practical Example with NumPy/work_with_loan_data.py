import numpy as np

np.set_printoptions(suppress=True, linewidth=100, precision=2)

# Setting these print options will ensure we don't often see rows of an array
# displayed over multiple lines

# Specifying these arguments won't alter the numerical values NumPy uses
# to compute mathematical operations

# Importing the Data
raw_data_np = np.genfromtxt("loan-data.csv", delimiter=';', skip_header=1)
print(raw_data_np)

# Checking for Incomplete Data

print(np.isnan(raw_data_np).sum())

temporary_fill = np.nanmax(raw_data_np) + 1 # A filler for all the missing entries
temporary_mean = np.nanmean(raw_data_np, axis=0) # Hold the means for every column

# Warnings don't prevent the code from compiling!

# There must exist entire columns full of only NaNs

# It looks like we have at least one empty column - It is not entirely true

# A column of only strings is automatically filled with NaNs (and considered "empty")

print(temporary_mean)
# Only store strings

# Any column with a mean of "nan" contains no numbers

temporary_stats = np.array([np.nanmin(raw_data_np, axis=0),
                            temporary_mean,
                            np.nanmax(raw_data_np, axis=0)])

print(temporary_stats)

# Splitting the Dataset

# Splitting the Columns

columns_strings = np.argwhere(np.isnan(temporary_mean)) # value != 0
# Column        mean    np.isnan()                      np.argwhere()
# contains =>    =   =>     =      =>   True != 0  =>   returns the
# only text     nan        True                             index

print(columns_strings)

columns_strings = np.argwhere(np.isnan(temporary_mean)).squeeze()
print(columns_strings)

columns_numeric = np.argwhere(np.isnan(temporary_mean) == False).squeeze()
print(columns_numeric)

# usecols = columns_strings
# usecols = columns_numeric

# Re-importing the Dataset
loan_data_strings = np.genfromtxt(
    "loan-data.csv",
    delimiter=';',
    skip_header=1,
    autostrip=True,
    usecols=columns_strings,
    # usecols=columns_numeric,
    dtype=np.str_,
)
print(loan_data_strings)
# The string dataset

loan_data_numeric = np.genfromtxt(
    "loan-data.csv",
    delimiter=';',
    skip_header=1,
    usecols=columns_numeric,
    autostrip=True,
    filling_values=temporary_fill
)
# We handle missing values among strings and numbers differently
print(loan_data_numeric)
# The numeric dataset

# The Names of the Columns
header_full = np.genfromtxt(
    "loan-data.csv",
    delimiter=';',
    skip_footer=raw_data_np.shape[0],
    autostrip=True,
    dtype=np.str_
)
print(header_full)

header_strings, header_numeric = header_full[columns_strings], header_full[columns_numeric]
print(header_strings)
print(header_numeric)

# Creating Checkpoints:

# Checkpoints:
# Places throughout our code where we store a copy of our dataset (or only parts of it)

# We want to avoid losing a lot of progress

# An extremely reliable practice when we need to clean or preprocess many parts of a dataset

# A failsafe we can rely on

def checkpoint(file_name, checkpoint_header, checkpoint_data):
    np.savez(file_name, header=checkpoint_header, data=checkpoint_data)
    checkpoint_variable = np.load(file_name + ".npz")
    return (checkpoint_variable)

checkpoint_test = checkpoint("checkpoint-test", header_strings, loan_data_strings)
print(checkpoint_test['header'])
print(checkpoint_test['data'])

print(np.array_equal(checkpoint_test['data'], loan_data_strings))

# Manipulating String Columns

print(header_strings)

header_strings[0] = "issue_date"

print(loan_data_strings)

# Issue Date

print(loan_data_strings[:, 0])

print(np.unique(loan_data_strings[:, 0]))
# Arranged in alphabetical oder, rather than chronologically

loan_data_strings[:, 0] = np.chararray.strip(loan_data_strings[:, 0 ], "-15")

print(np.unique(loan_data_strings[:, 0], "-15"))

# The (strip) function doesn't automatically remove these values

# In Analysis:
# Represent month values as integers

# Store the data using less memory (space)

# A more easy-to-follow order of the months

months = np.array(['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
# Both list and array are equally viable

for i in range(13):
    loan_data_strings[:, 0] = np.where(loan_data_strings[:, 0] == months[i],
                                       i,
                                       loan_data_strings[:, 0])

print(np.unique(loan_data_strings[:, 0]))

# We won't cast the values into integers right away

# Loan Status
print(header_strings)

print(loan_data_strings[:, 1])

print(np.unique(loan_data_strings[:, 1]))

print(np.unique(loan_data_strings[:, 1]).size)

# We can use np.where() to assign a different number to each one

# Regressions only care if the candidate is in a table financial condition

# We need to split all possible values into either group ("good" vs "bad")

# 1 "good"
# 0 "bad"

status_bad = np.array(['', 'Charged Off', 'Default', 'Late (31-120 days)'])

# It's important to write these values exactly like they appear in the "unique" array

loan_data_strings[:, 1] = np.where(np.isin(loan_data_strings[:, 1], status_bad))

print(np.unique(loan_data_strings[:, 1]))

# Term

print(header_strings)

print(np.unique(loan_data_strings[:, 2]))

loan_data_strings[:, 2] = np.chararray.strip(loan_data_strings[:, 2], " months")
print(loan_data_strings[:, 2])

header_strings[2] = 'term_months'

loan_data_strings[:, 2] = np.where(loan_data_strings[:, 2] == '',
                                   '60',
                                   loan_data_strings[:, 2])

# When we have missing data in CRM, we assume the worst

# 60 months (5 years) is the worst case here

print(loan_data_strings[:, 2])

print(np.unique(loan_data_strings[:, 2]))

# Grade and Subgrade

print(header_strings)

print(loan_data_strings[:, 3])
print(np.unique(loan_data_strings[:, 3]))

print(loan_data_strings[:, 4])
print(np.unique(loan_data_strings[:, 4]))

# Filling Sub Grade

for i in np.unique(loan_data_strings[:, 3])[1:]:
    loan_data_strings[:, 4] = np.where((loan_data_strings[:, 4] == '') & (loan_data_strings[:, 3] == i),
                                       i + 5,
                                       loan_data_strings[:, 4])

# *The column with index 4, rather than the forth column

print(np.unique(loan_data_strings[:, 4]))

# There are still rows of the dataset where we have neither the "sub_grade", not the "grade"

print(np.unique(loan_data_strings[:, 4], return_counts=True))

# We saw in Notepad++ that every column has 10,000 values

# We could drop these values and continue with our analysis

# We need to create a whole new category lower than G5

loan_data_strings[:, 4] = np.where(loan_data_strings[:, 4] == '',
                                   'H1',
                                   loan_data_strings[:, 4])

print(np.unique(loan_data_strings[:, 4]))
# We no longer have missing data in this column

# Removing Grade

loan_data_strings = np.delete(loan_data_strings, 3, axis=1)

print(loan_data_strings[:, 3])

header_strings = np.delete(header_strings, 3)

print(header_strings[3])

# Converting Sub Grade

print(np.unique(loan_data_strings[:, 3]))

# We don't want to manually use the np.where() function multiple times

keys = list(np.unique(loan_data_strings[:, 3]))
values = list(range(1, np.unique(loan_data_strings[:, 3]).shape[0] + 1))
dict_sub_grade = dict(zip(keys, values))

# If we don't add +1 at the end, we would only have 35 values (for 36 sub_grades)

print(dict_sub_grade)

for i in np.unique(loan_data_strings[:, 3]):
    loan_data_strings[:, 3] = np.where(loan_data_strings[:, 3] == i,
                                       dict_sub_grade[i],
                                       loan_data_strings[:, 3])

print(np.unique(loan_data_strings[:, 3]))

# Verification Status

print(header_strings)

print(loan_data_strings[:, 4])
print(np.unique(loan_data_strings[:, 4]))

# Loan applications which include investor backing

loan_data_strings[:, 4] = np.where((loan_data_strings[:, 4] == '') & (loan_data_strings[:, 4] == 'Not Verified'), 0, 1)

print(np.unique(loan_data_strings[:, 4]))

# URL

print(loan_data_strings[:, 5])

print(np.chararray.strip(loan_data_strings[:, 5], 'https://www.lendingclub.com/browse/loanDetail.action?loan_id='))

loan_data_strings[:, 5] = np.chararray.strip(loan_data_strings[:, 5], 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=4')

print(header_full)

print(loan_data_strings[:, 0])

print(loan_data_strings[:, 5])

print(loan_data_strings[:, 0].astype(dtype=np.int32))

print(loan_data_strings[:, 5].astype(dtype=np.int32))

print(np.array_equal(loan_data_strings[:, 0].astype(dtype=np.int32), loan_data_strings[:, 5].astype(dtype=np.int32)))

# The URL column doesn't hold any additional information we can't already extract from the ID column

loan_data_strings = np.delete(loan_data_strings, 5, axis=1)
header_strings = np.delete(header_strings, 5)

print(loan_data_strings[:, 5])

print(header_strings)

print(loan_data_numeric[:, 0])

print(header_numeric)

# State Address

print(header_strings)

header_strings[5] = "state_address"

print(loan_data_strings[:, 5])
print(np.unique(loan_data_strings[:, 5]))
print(np.unique(loan_data_strings[:, 5]).size)

# There are exactly 50 states in the USA

# We suspect lowa (IA) was purposefully left as a baseline benchmark

# When doing research or analysis on a variable with many categories,
# it is normal to pick one as a benchmark and include dummy variables
# for the rest

print(np.unique(loan_data_strings[:, 5], return_counts=True))

states_names, states_count = np.unique(loan_data_strings[:, 5], return_counts=True)
states_count_sorted = np.argsort(-states_count)
print(states_names[states_count_sorted], states_count[states_count_sorted])

# There are more applications with missing or unreported addresses than
# there are for 45 of the other states

# We have very little dat for too many states to examine each one individually

# If we assign a unique value to each state, this will allow outliers to have
# a big influence on the coefficients

# The more categories a variable has, the fewer data will be available for each one

loan_data_strings[:, 5] = np.where(loan_data_strings[:, 5] == '',
                                   0,
                                   loan_data_strings[:, 5])

states_west = np.array(['WA', 'OR', 'CA', 'NV', 'ID', 'MT', 'WY', 'UT', 'CO', 'AZ', 'NM', 'ΗΙ', 'ΑΚ'])
states_south = np.array(['TX', 'OK', 'AR', 'LA', 'MS', 'AL', 'TN', 'KY', 'FL', 'GA', 'SC', 'NC', 'VA', 'WV', 'MD', 'DE', 'DC'])
states_midwest = np.array(['ND', 'SD', 'NE', 'KS', 'MN', 'IA', 'MO', 'WI', 'IL', 'IN', 'MI', 'OH'])
states_east = np.array(['PA', 'NY', 'NJ', 'CT', 'MA', 'VT', 'NH', 'ME', 'RI'])

loan_data_strings[:, 5] = np.where(np.isin(loan_data_strings[:, 5], states_east), 1, loan_data_strings[:, 5])
loan_data_strings[:, 5] = np.where(np.isin(loan_data_strings[:, 5], states_south), 2, loan_data_strings[:, 5])
loan_data_strings[:, 5] = np.where(np.isin(loan_data_strings[:, 5], states_midwest), 3, loan_data_strings[:, 5])
loan_data_strings[:, 5] = np.where(np.isin(loan_data_strings[:, 5], states_west), 4, loan_data_strings[:, 5])

print(np.unique(loan_data_strings[:, 5]))

# We've converted whatever string data we had into numeric values stored as text

# Converting to Numbers

print(loan_data_strings)

print(loan_data_strings.astype(np.int_))

# None of the numbers (in loan_data_strings) are complex or even decimals

# This function will automatically assign the smallest datatype
# which successfully stores all these numbers

loan_data_strings = loan_data_strings.astype(np.int_)
print(loan_data_strings)

# Checkpoint 1: Strings

checkpoint_strings = checkpoint("Checkpoint-strings", header_strings, loan_data_strings)

print(checkpoint_strings["header"])
print(checkpoint_strings["data"])

print(np.array_equal(checkpoint_strings['data'], loan_data_strings))

# Manipulating Numeric Columns

print(loan_data_numeric)

print(np.isnan(loan_data_numeric).sum())

# There aren't any missing values in the array

# Substitute "Filler" Values

print(header_numeric)

# ID

# We must check whether any of the elements of this column equal the temporary_fill

print(temporary_fill)

print(np.isin(loan_data_numeric[:, 0], temporary_fill))

print(np.isin(loan_data_numeric[:, 0], temporary_fill).sum())

print(header_numeric)

# Temporary Stats

print(temporary_stats)
# print(temporary_stats[:, header_numeric]) error
# Unlike series, arrays only rake numerical indices

print(temporary_stats[:, columns_numeric])

# Funded Amount

print(loan_data_numeric[:, 2])

loan_data_numeric[:, 2] = np.where(loan_data_numeric[:, 2] == temporary_fill,
                                   temporary_stats[0, columns_numeric[2]],
                                   loan_data_numeric[:, 2])
print(loan_data_numeric[:, 2])

print(temporary_stats[0, 3])

# Even though we converted the values of loan_status earlier,
# we generated temporary_stats even before that

print(temporary_stats[0, columns_numeric[3]])

# Loaned Amount, Interest Rate, Total Payment, Installment

# Filling out the remaining numeric columns according to the Head
# of Data Analytics' casting directions

print(header_numeric)

for i in [1, 3, 4, 5]:
    loan_data_numeric[:, i] = np.where(loan_data_numeric[:, i] == temporary_fill,
    temporary_stats[2, columns_numeric[i]], loan_data_numeric[:, i])

print(loan_data_numeric)

# Currency Change

# The Exchange Rate

EUR_USD = np.genfromtxt("EUR-USD.csv", autostrip=True)
print(EUR_USD) # First row - Provably the names of the columns

EUR_USD = np.genfromtxt("EUR-USD.csv", autostrip=True, dtype=np.str_)
print(EUR_USD)

# We can't really vuy or sell the exchange rate itself

print(loan_data_strings[:, 0])

exchange_rate = loan_data_strings[:, 0]
for i in range(1, 13):
    exchange_rate = np.where(exchange_rate == i,
                             EUR_USD[i-1], # Indexing in Python starts from 0
                             exchange_rate)

exchange_rate = np.where(exchange_rate == 0,
                         np.mean(EUR_USD),
                         exchange_rate)
print(exchange_rate)

print(exchange_rate.shape)

print(loan_data_numeric.shape)

exchange_rate = np.reshape(exchange_rate, (10000, 1))

print(np.hstack((loan_data_numeric, exchange_rate)))

loan_data_numeric = np.hstack((loan_data_numeric, exchange_rate))

# header_numeric = np.concatenate((header_numeric, 'exchange_rate')) error
header_numeric = np.concatenate((header_numeric, np.array(['exchange_rate'])))
print(header_numeric)

# From USD to EUR

print(header_numeric)

columns_dollar = np.array([1, 2, 4, 5])

print(loan_data_numeric[:, [columns_dollar]])

for i in columns_dollar:
    # loan_data_numeric - np.hstack((loan_data_numeric, loan_data_numeric[:, i] / loan_data_numeric[:, 6])) error
    loan_data_numeric - np.hstack((loan_data_numeric, np.reshape(loan_data_numeric[:, i] / loan_data_numeric[:, 6], (10000, 1))))

print(loan_data_numeric[:, 6])

print(loan_data_numeric.shape)

print(loan_data_numeric)

# Expanding the header

header_additional = np.array([column_name + '_EUR' for column_name in header_numeric[columns_dollar]])
print(header_additional)

header_numeric = np.concatenate((header_numeric, header_additional))
print(header_numeric)

header_numeric[columns_dollar] = np.array([column_name + '_USD' for column_name in header_numeric[columns_dollar]])
print(header_numeric)

# We will rearrange the columns to that each EUR column follows its corresponding USD column

columns_index_order = [0, 1, 7, 2, 8, 3, 4, 9, 5, 10, 6]

print(header_numeric[columns_index_order])

header_numeric = header_numeric[columns_index_order]

print(loan_data_numeric)

print(loan_data_numeric[:, columns_index_order])

loan_data_numeric = loan_data_numeric[:, columns_index_order]

# Interest Rate

print(header_numeric)

print(loan_data_numeric[:, 5])

# The convention usually dictates using values between 0 and 1

print(loan_data_numeric[:, 5] / 100)

loan_data_numeric[:, 5] = loan_data_numeric[:, 5] / 100

print(loan_data_numeric[:, 5])

# Checkpoint 2: Numeric

checkpoint_numeric = checkpoint("Checkpoint-Numeric", header_numeric, loan_data_numeric)

print(checkpoint_numeric['header'], checkpoint_numeric['data'])

# Creating the "Complete" Dataset

# The two arrays must have compatible shapes

print(checkpoint_strings['data'].shape)

print(checkpoint_numeric['data'].shape)

print(np.hstack((checkpoint_numeric['data'], checkpoint_strings['data'])).shape)

loan_data = np.hstack((checkpoint_numeric['data'], checkpoint_strings['data'])).shape
print(loan_data)

print(np.isnan(loan_data).sum())
# We expect to see 0 since we took care of them earlier in the practical example

print(np.concatenate((checkpoint_numeric['header'], checkpoint_strings['header'])))

header_full = np.concatenate((checkpoint_numeric['header'], checkpoint_strings['header']))

# Sorting the New Dataset

# We want to rearrange the entire dataset according to the values in the first column

print(loan_data[:, 0])

print(np.sort(loan_data[:, 0]))

print(loan_data[np.argsort(loan_data[:, 0])])

loan_data = loan_data[np.argsort(loan_data[:, 0])]
print(loan_data)

print(np.argsort(loan_data[:, 0]))

# Storing the New Dataset

print(np.vstack((header_full, loan_data)))

# The stack requires a unified datatype across all rows and columns

# THe function selects the smallest datatype which can hold any of the elements within the array

np.savetxt("loan-data-preprocessed.csv", loan_data, fmt='%s', delimiter=',')

# The function stores the values in an external file rather display them on screen

# We've successfully managed to:
# 1.) clean the dataset
# 2.) preprocess the dataset
# 3.) prepare the dataset for further analysis

# Our data science team can take this dataset and create a CRM fro estimating probability of default - Instructor