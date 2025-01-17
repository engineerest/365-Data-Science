from langchain_core.runnables import RunnableLambda

find_sum = lambda x: sum(x)

print(find_sum([1, 2, 5]))

find_square = lambda x: x**2

print(find_square(8))

runnable_sum = RunnableLambda(lambda x: sum(x))
# runnable_sum = RunnableLambda(find_sum)

# Lambda Functions = Anonymous Functions

print(runnable_sum.invoke([1, 2, 5]))

runnable_square = RunnableLambda(lambda x: x**2)

print(runnable_square.invoke(8))

chain = runnable_sum | runnable_square

print(chain.invoke([1, 2, 5]))

chain.get_graph().print_ascii()

# RunnableLambda
# Allows us to convert any function into a Runnable
# that we can then invoke and enter as a chain component.