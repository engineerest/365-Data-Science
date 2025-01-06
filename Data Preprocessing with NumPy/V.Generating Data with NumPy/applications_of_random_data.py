from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg
import numpy as np

array_RG = gen(pcg(seed=365))

array_column_1 = array_RG.normal(loc=2, scale=3, size=(1000))
array_column_2 = array_RG.normal(loc=7, scale=2, size=(1000))
array_column_3 = array_RG.logistic(loc=11, scale=3, size=(1000))
array_column_4 = array_RG.exponential(scale=4, size=(1000))
array_column_5 = array_RG.geometric(p=0.7, size=(1000))

random_test_data = np.array([array_column_1, array_column_2, array_column_3, array_column_4, array_column_5])
print(random_test_data)

print(random_test_data.shape)

np.savetxt("Random-Test-from-NumPy.csv", random_test_data, fmt='%s', delimiter=',')
np.genfromtxt("Random-Test-from-NumPy.csv", delimiter=',')
