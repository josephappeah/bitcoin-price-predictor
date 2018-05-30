# ECE 492: Senior Design - Group 11
# Bitcoin Price Predictor - Polynomial Regression w/ MultiFeature
# 11/17/17

from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import quandl
import data
import pca

# Set Parameters
learning_rate = 0.3  # Cost function learning rate
reg_param = 0.9  # Regularization Parameter
training_epochs = 20000  # Number of iterations of Gradient Descent
display_step = 1000  # Display Step
testing_days = 1
np.random.seed(0)
random = np.random
p = 20  # Polynomial Power
n = 6  # Number of Features

# Get market price
_, Y = data.get_data("BCHAIN/MKPRU", 365)

# Number of training examples
m = Y.shape[0]-testing_days

# Principal Component Analysis - get features
Z = pca.pca().reshape((365, n))

# Split into training and testing
train = Z[:365-testing_days, :]
train_label = Y[:365-testing_days]
test = Z[365-testing_days:]
test_label = Y[365-testing_days:]


# Mean Normalization and Feature Scaling
train_X = np.zeros([n*p, m])
test_X = np.zeros([n*p, testing_days])
for i in range(n):
    for j in range(p):
        train_temp = np.power(train[:, i], j+1)
        test_temp = np.power(test[:, i], j+1)
        train_X[i*p+j, :] = (train_temp - np.mean(train_temp)) / np.std(train_temp, axis=0)
        test_X[i*p+j, :] = (test_temp - np.mean(train_temp)) / np.std(train_temp, axis=0)

# Set model weight and bias
theta = tf.Variable(tf.cast(tf.random_uniform([1, n*p], -1.0, 1.0), tf.float64), name="theta")
bias = tf.Variable(tf.cast(tf.random_uniform([1], -1.0, 1.0), tf.float64), name="bias")

# Hypothesis of Market Price
hypothesis = tf.matmul(theta, train_X) + bias

# Mean Squared Error
regularization = reg_param * tf.matmul(theta, tf.transpose(theta))
cost = tf.reduce_mean((tf.square(hypothesis - train_label) + regularization) / (2 * m))

# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Start Tensorflow session
with tf.Session() as S:

    # Initializer
    S.run(tf.global_variables_initializer())

    # Training data
    for epoch in range(training_epochs):
        S.run(optimizer)

    hypothesis = tf.matmul(theta, test_X) + bias

    # Save date
    date = np.array([])
    dates = quandl.get("BCHAIN/MWNUS", returns="numpy")[-testing_days:]

    for day in dates:
        date = np.append(date, day[0].strftime("%m/%d/%Y"))

    output = np.array([])
    for i in range(len(test_label)):
        val = str(date[i]) + "," + str(test_label[i]) + "," + str(S.run(hypothesis)[0][i])
        output = np.append(output, val)

    np.savetxt('poly_NEXTDAY', output, fmt='%s', delimiter=',')
