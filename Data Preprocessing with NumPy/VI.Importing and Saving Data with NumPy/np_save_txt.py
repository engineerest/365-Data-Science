import numpy as np

lending_co = np.genfromtxt("Lending-Company-Saving.csv", delimiter=',', dtype=np.str_)

# np.savetxt()
# Helps store NumPy datasets in text files

# .txt ot.csv

# The syntax is once again vary familiar to np.save() and np.savez()

np.savetxt('Lending-Company-Saving.txt', lending_co, fmt='%s', delimiter=',')

lending_data_savetxt = np.genfromtxt("Lending-Company-Saving.txt", delimiter=',', dtype=np.str_)
print(lending_data_savetxt)
# np.savetxt() requires importing the file

lending_data_save = np.load("Lending-Company-Saving.npy")
print(np.array_equal(lending_data_savetxt, lending_data_save))

# Both functions produce equivalent results

# These restrictions have enabled .npy files to be much more efficient

# It's important to know how to use both approaches (.npy vs .csv/.txt)