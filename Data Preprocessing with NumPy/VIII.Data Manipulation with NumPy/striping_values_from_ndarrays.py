import numpy as np

# Stripping Data
lending_co_total_price = np.genfromtxt("Lending-Company-Total-Price.csv",
                                       delimiter=",",
                                       dtype=np.str_,
                                       skip_header=1,
                                       usecols=[1, 2, 4])

print(lending_co_total_price)

# We only want the columns which contain non-numeric data

# We'll be stripping each column of these excess strings

# Stripping
# Removing specific parts of string

# Not straight up deleting the values stored in specific positions...
# ..but rather taking away small parts

# It allows us to get rid of excess data

lending_co_total_price[:, 0] = np.chararray.strip(lending_co_total_price[:, 0], "id_")
lending_co_total_price[:, 1] = np.chararray.strip(lending_co_total_price[:, 1], "Product")
lending_co_total_price[:, 2] = np.chararray.strip(lending_co_total_price[:, 2], "Location")
print(lending_co_total_price)

# We can also apply np.where to transform
# the letters in the second column into numeric values

lending_co_total_price[:, 1] = np.where(lending_co_total_price[:, 1] == 'A', 1, lending_co_total_price[:, 1])
lending_co_total_price[:, 1] = np.where(lending_co_total_price[:, 1] == 'B', 2, lending_co_total_price[:, 1])
lending_co_total_price[:, 1] = np.where(lending_co_total_price[:, 1] == 'C', 3, lending_co_total_price[:, 1])
lending_co_total_price[:, 1] = np.where(lending_co_total_price[:, 1] == 'D', 4, lending_co_total_price[:, 1])
lending_co_total_price[:, 1] = np.where(lending_co_total_price[:, 1] == 'E', 5, lending_co_total_price[:, 1])
lending_co_total_price[:, 1] = np.where(lending_co_total_price[:, 1] == 'F', 6, lending_co_total_price[:, 1])

print(lending_co_total_price)

# Quotation marks around numeric values mean these are strings that
# only look like numeric values

lending_co_total_price = lending_co_total_price.astype(dtype=np.int32)

# We've managed to completely transform an array
# of text into a clean array of numeric values