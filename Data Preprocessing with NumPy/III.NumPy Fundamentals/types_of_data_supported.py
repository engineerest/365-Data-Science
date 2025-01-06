import numpy as np

array_a = np.array([[1, 2, 3], [4, 5, 6]])
print(array_a)

# array_a = np.array([[1, 2, 3], [4, 5, 6]], dtype="float32") # 32 bits of memory for each element of the array
# We can't put just any random number at the end of the type

array_a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32) # np.data_type = "data_type"

# Good practice dictates sticking to a consistent notation (np.float32 or "float32")
print(array_a)
# Data Types for arrays:
# Arrays can contain numbers
# All the numerical datatypes supported by C

# We don't have actual decimal values in our original dataset

array_a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.complex64)
# 7.3(real) + 1.2j(imaginary)
print(array_a)

# Even though the output looks different, we are essentially still storing the same data

array_a = np.array([[1, 2, 0], [4, 5, 6]], dtype=np.str_)
print(array_a)

# The actual symbols that express each digit, rather than the numeric values we have examined so fat
# Unicode values of length up to 1
