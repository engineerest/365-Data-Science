import numpy as np

lending_co = np.genfromtxt("Lending-Company-Saving.csv", delimiter=',', dtype=np.str_)
lending_data_save = np.load('Lending-Company-Saving.npy')

# np.savez()

# Doesn't create an .npy, but an .npz
# The NPZ is like an archive of NPYs that can store multiple arrays
# Instead of storing different datasets in separate NPY files, we can store all of them in a single NPZ
# NPZs can be very useful when working with large amounts of data

np.savez("Lending-Company-Saving", lending_co, lending_data_save)
lending_data_savez = np.load('Lending-Company-Saving.npz')
print(lending_data_savez)
# The NPZ contained a collection of arrays
# It can't properly displayed this way

print(lending_data_savez["arr_0"])
# ["arr_0"] = [0]

# Python uses 0-indexing, so "arr_0" refers to the first array we stored in the NPZ

print(lending_data_savez["arr_1"])

# By default, the NPZ files stores each dataset as a separate array with a generic name

np.savez('Lending-Company-Saving', lending_co, data_save=lending_data_save)
lending_data_savez = np.load('Lending-Company-Saving.npz')
print(lending_data_savez.files)

# We no longer need to use the generic "arr_0" and "arr_1" notation

print(lending_data_savez["arr_0"])

print(lending_data_savez["data_save"])

print(np.array_equal(lending_data_savez["arr_0"], lending_data_savez["data_save"]))