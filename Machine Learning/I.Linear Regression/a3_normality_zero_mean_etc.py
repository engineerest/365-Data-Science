import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = pd.read_csv('Assumption_3.csv') # it is example code. Because Instructor didn't submit csv data

data['log_x'] = np.log(data['x'])
data['log_y'] = np.log(data['y'])

plt.scatter(data['x'], data['y'])
plt.xlabel('X')
plt.ylabel('Y')

# The model - yhat = b0 + b1*x1


plt.scatter(data['log_x'], data['y'])
plt.xlabel('Log X')
plt.ylabel('Y')
# Semi-log model:
# yhat = b0 + b1*(logx1)

plt.scatter(data['x'], data['log_y'])
plt.xlabel('X')
plt.ylabel('Log Y')
# Semi-log model:
# log yhat = b0+b1*x1
# As X increases by 1 unit, Y increases by b1 percent

plt.scatter(data['log_x'], data['log_y'])
plt.xlabel('Log X')
plt.ylabel('Log Y')
#Log-log model:
# log yhat = b0 + b1*(logx1)
# As X increases by 1 percent
# Y increases by b1 percent
# elasticity

plt.show()

