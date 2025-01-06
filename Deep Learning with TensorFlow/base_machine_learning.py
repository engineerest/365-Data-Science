# Import the relevant libraries

import numpy as np
import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as plt

# Data generation

observations = 1000

xs = np.random.uniform(-10, 10, (observations, 1))
zs = np.random.uniform(-10, 10, (observations, 1))

generated_inputs = np.column_stack((xs, zs))

noise = np.random.uniform(-1, 1, (observations, 1))

generated_targets = 2*xs + 3*zs + 5 + noise

np.savez('TF_intro', inputs=generated_inputs, targets=generated_targets)

# Solving with TensorFlow

training_data = np.load('TF_intro.npz')

input_size = 2
output_size = 1

model = tf.keras.Sequential([
    tf.keras.layers.Dense(output_size,
                          kernel_initializer=tf.random_uniform_initializer(-0.1, 0.1),
                          bias_initializer=tf.random_uniform_initializer(-0.1, 0.1)),
])
# tf.keras.layers.Dense(output_size, kernel_initializer, bias_initializer) function that is laying down
# the model (used to 'stack layers') and initialize weights

custom_optimizer = tf.keras.optimizers.SGD(learning_rate=0.02)
# tf.keras.optimizers.SGD(learning_rate) Stochastic gradient descent optimizers,
# including support for learning rate, momentum, decay, etc.

# model.compile(optimizer='sgd', loss='mean_squared_error')
model.compile(optimizer=custom_optimizer, loss='mean_squared_error')

model.fit(training_data['inputs'], training_data['targets'], epochs=100, verbose=2)

# Extract the weights and bias

print(model.layers[0].get_weights())
weights = model.layers[0].get_weights()[0]
print(weights)

bias = model.layers[0].get_weights()[1]
print(bias)

# Extract outputs (make predictions)

print(model.predict_on_batch(training_data['inputs']).round(1))
# model.predict_on_batch(data) calculates the outputs given inputs

print(training_data['targets'].round(1))

# Plotting the data

plt.plot(np.squeeze(model.predict_on_batch(training_data['inputs'])), np.squeeze(training_data['targets']))
plt.xlabel('outputs')
plt.ylabel('inputs')
plt.show()
