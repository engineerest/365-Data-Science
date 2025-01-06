# Substituting Missing Values

import numpy as np

# Last time:
# An array where all values are numeric
# All "missing values" are equal to the maximum of this array
# If a value is equal to the maximum of the array,
# it's actually a "missing" value

# Fill all missing values
# with the mean:
# This won't change the overall interpretation of the dataset
# All missing values would be considered average
# Not always valid

lending_co_data_numeric_NAN = np.genfromtxt("Lending-company-Numeric-NAN.csv", delimiter=';')
print(lending_co_data_numeric_NAN)

temporary_mean = np.nanmean(lending_co_data_numeric_NAN, axis=0).round(2)
# We want to keep track of the different means because they can change after filling out the missing elements

print(temporary_mean[0])

temporary_fill = np.nanmax(lending_co_data_numeric_NAN).round(2) + 1
lending_co_data_numeric_NAN = np.genfromtxt("Lending-company-Numeric-NAN.csv",
                                            delimiter=";",
                                            filling_values=temporary_fill)

print(temporary_fill)


print(np.mean(lending_co_data_numeric_NAN[:, 0]).round(2))

print(temporary_mean[0])

lending_co_data_numeric_NAN[:, 0] = np.where(lending_co_data_numeric_NAN[:, 0] == temporary_fill,
                                             temporary_mean[0],
                                             lending_co_data_numeric_NAN[:, 0])

print(np.mean(lending_co_data_numeric_NAN[:, 0]).round(2))
# Whenever we add the mean of a set to itself,
# the mean of the new set stays the same

# Example:
# a_1 = [1, 2, 3]
# 1 + 2 + 3 = 6
# 6/3 = 2
# a_2 = [1, 2, 2, 3]
# 1 + 2 + 3 + 2 = 8
# 8/4 = 2

for i in range(lending_co_data_numeric_NAN.shape[1]):
    lending_co_data_numeric_NAN[:, i] = np.where(lending_co_data_numeric_NAN[:, i] == temporary_fill,
                                                 temporary_mean[i],
                                                 lending_co_data_numeric_NAN[:, i])

    for i in range(lending_co_data_numeric_NAN.shape[1]):
        lending_co_data_numeric_NAN[:, i] = np.where(lending_co_data_numeric_NAN[:, i] < temporary_fill,
                                                     0,
                                                     lending_co_data_numeric_NAN[:, i])


