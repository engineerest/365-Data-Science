from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg

array_RG = gen(pcg(seed=365))
# We need to declare the seed every time

print(array_RG.poisson(size=(5, 5))) # lambda = 1

# Over a fixed interval of time, distance, or space we expect an event to occur exactly once

array_RG = gen(pcg(seed=365))
print(array_RG.poisson(lam=10, size=(5, 5)))
# 25 times because we have a 5 by 5 array and 5*5=25

# "other 24 indentical experiments" because we have a total of 25 and already commented on 1

# We have 9 different outcomes rather than 3

# Fixing our expectations for obtaining 10 features for every experiment is NOT realistic

# Binomial distribution
# Measures how many times a certain outcome can appear over a series of trials,
# where there are only 2 possible outcomes

array_RG = gen(pcg(seed=365))

# Binomial distribution
# n - number of trials
# p - probability of getting our desired outcome

print(array_RG.binomial(n=100, p=0.4, size=(5, 5)))

array_RG = gen(pcg(seed=365))
print(array_RG.logistic(loc=9, scale=1.2, size=(5, 5)))

# Logistic distribution
# Each element is a possible outcome of a logistic distribution with loc=9 and scale=1.2
