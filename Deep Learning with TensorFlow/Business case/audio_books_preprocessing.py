# Extract data from the csv
import numpy as np
from sklearn import preprocessing # 10 percent gain for this problem

# I will use the sklearn capabilities for standardizing the inputs
# Almost always we standardize all inputs

raw_data_csv = np.loadtxt('Audiobooks_data.csv', delimiter=',')

unscaled_inputs_all = raw_data_csv[:, 1:-1]
targets_all = raw_data_csv[:, -1]

# Balance the dataset

# If we sum all the targets we will get the number of targets that are 1s

num_one_targets = int(np.sum(targets_all))
zero_targets_counter = 0
indices_to_remove = []

for i in range(targets_all.shape[0]): # The shape of targets_all on axis = 0, is basically the length of the vector
    if targets_all[i] == 0:
        zero_targets_counter += 1
        if zero_targets_counter > num_one_targets:
            indices_to_remove.append(i)

unscaled_inputs_equal_priors = np.delete(unscaled_inputs_all, indices_to_remove, axis=0)
# np.delete(array, obj to delete, axis) is a method that deletes an object along an axis
targets_equal_priors = np.delete(targets_all, indices_to_remove, axis=0)

# Standardize the inputs
scaled_inputs = preprocessing.scale(unscaled_inputs_equal_priors)
# preprocessing.scale(X) is a method that standardizes an array along an sklearn

# Shuffle the data

# A little trick is to shuffle the inputs and the targets.
# We keep the same information but in a random order

# Since we will be batching, we must shuffle the data
shuffled_indices = np.arange(scaled_inputs.shape[0])
# np.arange([start], stop) is a method that returns a evenly spaced values withing a given interval
np.random.shuffle(shuffled_indices)
# np.random.shuffle(X) is a method that shuffles the numbers in a given sequence

shuffled_inputs = scaled_inputs[shuffled_indices]
shuffled_targets = targets_equal_priors[shuffled_indices]

# Split the dataset into train, validation, and test

samples_count = shuffled_inputs.shape[0]

# I will use the 80-10-10 split for train, validation, and test

train_samples_count = int(0.8 * samples_count)
validation_samples_count = int(0.1 * samples_count)
test_samples_count = samples_count - train_samples_count - validation_samples_count

# We have the sizes of the train, validation, and test. Let's extract them

train_inputs = shuffled_inputs[:train_samples_count]
train_targets = shuffled_targets[:train_samples_count]

validation_inputs = shuffled_inputs[train_samples_count:train_samples_count + validation_samples_count]
validation_targets = shuffled_targets[train_samples_count:train_samples_count + validation_samples_count]

test_inputs = shuffled_inputs[train_samples_count+validation_samples_count:]
test_targets = shuffled_targets[train_samples_count+validation_samples_count:]
# It is useful to check if we have balanced the dataset

print(np.sum(train_targets), train_samples_count, np.sum(train_targets) / train_samples_count)
print(np.sum(validation_targets), validation_samples_count, np.sum(validation_targets) / validation_samples_count)
print(np.sum(test_targets), test_samples_count, np.sum(test_targets) / test_samples_count)

# Save the three datasets in *.npz

np.savez('Audiobooks_data_train', inputs=train_inputs, targets=train_targets)
np.savez('Audiobooks_data_validation', inputs=validation_inputs, targets=validation_targets)
np.savez('Audiobooks_data_test', inputs=test_inputs, targets=test_targets)
# Each time we run the code in this sheet, we will preprocess the data once again (forgetting the previous preprocessing)
# You can use this same code to preprocess any dataset that has two classes