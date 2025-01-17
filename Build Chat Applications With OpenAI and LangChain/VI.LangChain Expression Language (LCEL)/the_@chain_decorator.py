from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import chain

def find_sum(x):
    return sum(x)

def find_square(x):
    return x**2

chain1 = RunnableLambda(find_sum) | RunnableLambda(find_square)
print(chain1.invoke([1, 2, 5]))

@chain
def runnable_sum(x):
    return sum(x)

# Decorator
# A function that modifies the behavior of another function or a class,
# enhancing their functionality

# Decorator
# RunnableLambda(runnable_sum)

# @chain
# Elegant and intuitive
# The function's name also set at the name of the runnable.

@chain
def runnable_square(x):
    return x**2

# Avoid naming your variables 'chain'.

print(type(runnable_sum), type(runnable_square))

chain2 = runnable_sum | runnable_square
print(chain2.invoke([1, 2, 5]))