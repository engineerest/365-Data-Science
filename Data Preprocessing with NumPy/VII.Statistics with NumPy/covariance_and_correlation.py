import numpy as np

matrix_a = np.array([[1, 0, 0, 3, 1], [3, 6, 6, 2, 9], [4, 5, 3, 8, 0]])
print(matrix_a)

# np.cov()

# Requires a single input variable: the dataset

print(np.cov(matrix_a))

# Cov(X, X) = Var(X)

# Cov(A, B) = Cov(B, A)

# Correlation
# Corr(X, Y) = Cov(X, Y) / sigmaX * sigmaY
# Expect a symmetrical matrix
# corrcoef = correlation coefficient
# Finds the relationships between every two rows of the array

print(np.corrcoef(matrix_a))
# Corr(X, X) = 1