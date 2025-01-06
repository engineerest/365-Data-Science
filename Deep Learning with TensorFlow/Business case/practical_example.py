# Create the machine learning algorithm

# Import the relevant libraries

import numpy as np
import tensorflow as tf

# Data

npz = np.load('Audiobooks_data_train.npz')

train_inputs = npz['inputs'].astype(np.float32)
# We expect all inputs to be floats
# np.ndarray.astype() creates a copy of the array, cast to a specific type
train_targets = npz['targets'].astype(np.int32)
# Our targets are only 0s and 1s, but we are not completely certain about their data type

npz = np.load('Audiobooks_data_validation.npz')
validation_inputs, validation_targets = npz['inputs'].astype(np.float32), npz['targets'].astype(np.int32)

# Test data
npz = np.load('Audiobooks_data_test.npz')
test_inputs, test_targets = npz['inputs'].astype(np.float32), npz['targets'].astype(np.int32)

# Unlike, our train,validation, and test is simply in array form

# Model

# Outline, optimizers, loss, early stoppung and training

input_size = 10
output_size = 2
hidden_layer_sze = 50

model = tf.keras.Sequential([
    tf.keras.layers.Dense(hidden_layer_sze, activation='relu'),
    tf.keras.layers.Dense(hidden_layer_sze, activation='relu'),
    tf.keras.layers.Dense(output_size, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

batch_size = 100

max_epochs = 100

early_stopping = tf.keras.callbacks.EarlyStopping(patience=120)
# tf.keras.callbacks.EarlyStopping(patience) configures the early stopping mechanism of the algorithm.
# 'patience' lets us decide how many consecutive increases we can tolerate

# If we are given 10 customers an their audiobook activity we will be able to correctly identify future customer behavior of 9 of them

# By default, this object will monitor the validation loss and stop the training process the first time the validation loss starts increasing

model.fit(train_inputs, train_targets,
          batch_size=batch_size, epochs=max_epochs,
          validation_data=(validation_inputs, validation_targets),
          verbose=2, callbacks=[early_stopping])
# Indicating the batch size in .fit() will automatically batch the data

# It is extremely hard to predict human behavior..
# The ML algorithm we create here is a new tool in your arsenal that has given you an incredible edge!

# Test the model

test_loss, test_accuracy = model.evaluate(test_inputs, test_targets)
# model.evaluate() returns the loss value and metrics values for the model in 'test mode'
print('Test loss:', test_loss)
print('Test accuracy:', test_accuracy*100)

weights, bias = model.layers[0].get_weights()
print("weights: {}".format(weights))
print("bias: {}".format(bias))

