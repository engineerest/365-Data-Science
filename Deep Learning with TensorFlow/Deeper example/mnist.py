# Import the relevant packages

import numpy as np
import pandas as pd

import tensorflow as tf
import tensorflow_datasets as tfds

# Data

mnist_dataset, mnist_info = tfds.load(name='mnist', with_info=True, as_supervised=True)
# tfds.load(name) loads a dataset from TensorFlow datasets

# tfds.load(name, as_supervised) loads a dataset form TensorFlow datasets -> as_supervised = True,
# loads the data in a 2-tuple structure [input, target]

# tfds.load(name, with_info, as_supervised) loads a dataset from TensorFlow datasets -> as_supervised = True,
# loads the data in a 2-tuple structure [input, target]
# -> with_info = True, provides a tuple containing info about version, features, # samples of the dataset

mnist_train, mnist_test = mnist_dataset['train'], mnist_dataset['test']

num_validation_samples = 0.1 * mnist_info.splits['train'].num_examples
num_validation_samples = tf.cast(num_validation_samples, tf.int64)
# tf.cast(x, type) casts (converts) a variable into a given data type

num_test_samples = mnist_info.splits['test'].num_examples
num_test_samples = tf.cast(num_test_samples, tf.int64)

# Normally, we'd like to scale our data in some way to make the result more numerically stable (e.g. inputs between 0 and 1)

# function to scale the integers
def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255
    # if the value / 255, to
    # 152 converts to 0.59
    # 255 converts to 1.0
    return image, label


# dataset.map(*function*) applies a custom transformation to a given dataset.
# It takes as input a function which determines the transformation

scaled_train_and_validation_data = mnist_train.map(scale)
test_data = mnist_test.map(scale)

# Shuffle the data

# Shuffling is a little trick we like to apply in the pre-processing stage
# Shuffling = Keeping the same information but in a different order

BUFFER_SIZE = 10000
# When we are dealing with enormous datasets, we can't shuffle all data at once
# If buffer_size = 1, no shuffling will actually happen
# If buffer_size >= num_samples, shuffling will happen at once (uniformly)
# If 1 < buffer_size < num_samples, we will be optimizing the computational power

shuffled_train_and_validation_data = scaled_train_and_validation_data.shuffle(BUFFER_SIZE)

validation_data = shuffled_train_and_validation_data.take(num_validation_samples)
train_data = shuffled_train_and_validation_data.skip(num_validation_samples)

# batch size = 1 = Stochastic gradient descent (SGD)
# batch size = # samples = (single batch) GD

BATCH_SIZE = 100

# dataset.batch(batch_size) a method that combines the consecutive elements of a dataset into batches

train_data = train_data.batch(BATCH_SIZE)
validation_data = validation_data.batch(num_validation_samples)
test_data = test_data.batch(num_test_samples)

# When batching we find the AVERAGE loss

validation_inputs, validation_targets = next(iter(validation_data))
# next() loads the next element of an iterable object
# iter() creates an object which can be iterated one element at a time (e.g. in a for loop or while loop)

# Model

# Outline the model

input_size = 784
output_size = 10
hidden_layer_size = 200 #100 #50

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28, 1)),
    tf.keras.layers.Dense(hidden_layer_size, activation='relu'),
    tf.keras.layers.Dense(hidden_layer_size, activation='relu'),
    # As you can see, outlining the model is a child's play
    tf.keras.layers.Dense(output_size, activation='softmax')
    # softmax -> good
    # sigmoid -> average
    # tanh -> bad
])
# tf.keras.layers.Flatten(original shape) transforms (flattens) a tensor into a vector
# tf.keras.layers.Dense(output size) takes the inputs, provided to the model and calculates the dot product of the inputs
# and the weights and adds the bias. This is also where we can apply an activation function

# Choose the optimizer and the loss function

# One fo the best choices we've got is the adaptive moment estimation (Adam)

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# These strings are NOT case sensitive

# losses:
# binary_crossenttropy
# categorical_crossentropy -> expects that you've one-hot encoded the targets
# sparse_categorical_crossentropy -> applies one-hot encoding


# model.compile(optimizer, loss) configures the model for training

# Training

NUM_EPOCHS = 5

model.fit(train_data, epochs=NUM_EPOCHS, validation_data=(validation_inputs, validation_targets), verbose=2)

# WHAT HAPPENS INSIDE AN EPOCH
# 1. At the beginning of each, the training loss will be set to 0
# 2. The algorithm will iterate over a preset number of batches, all from train_data
# 3. The weights and biases will be updated as many times as there are batches
# 4. We will get a value for the loss function, indicating how the training is going
# 5. We will also see a training accuracy
# *When we reach the maximum number of epochs the raining will be over

# We achieved an accuracy of 97.90%!!!

# Test the model

test_loss, test_accuracy = model.evaluate(test_data)
# model.evaluate() returns the loss value and metrics values for the model in 'test mode'
print('Testing:')
print('Test loss:', test_loss)
print('Test accuracy:', test_accuracy*100) # in percent