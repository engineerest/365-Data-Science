import numpy as np

lending_co = np.genfromtxt("Lending-Company-Saving.csv", delimiter=',', dtype=np.str_)
print(lending_co)

# np.save()
# np.save("file-name", dataset_variable)

# A name that clearly depicts the data we're storing

np.save("Lending-Company-Saving", lending_co)

# np.save()
# Creates an "file-name.npy" file in the same directory (folder) as your notebook (.ipytnb) (code printed in Pycharm!) document
# NPY is a special type of text file native to NumPy
# NPY is much faster
# NPY files take up way less memory space

# NPY vs CSV
# 1.) Faster to work with
# 2.) More compact

# CSVs (and other text files) are still extremely useful when preprocessing
# and analyzing data with other libraries (or programing languages)

# load a dataset =/= import a dataset

# Importing doesn't keep track of the datatype of the original array

# We may need to specify the datatype of the values after having brought them into Python

# When loading, we don't need to specify or change our data while working with our Python object

# The most convenient feature of NPY:
# The entire dataset keeps its format
# We don't need to worry about specifying and reorganizing the values from the external text file

# Suppose
# We store certain parts of the dataset as numbers
# NPY is technically a text file
# When we load the dataset back into Python...
# ... it will consider them as numbers automatically

lending_data_save = np.load("Lending-Company-Saving.npy")
print(lending_data_save)

print(np.array_equal(lending_data_save, lending_co))
# The data is unaltered after we saved it and loaded it back in