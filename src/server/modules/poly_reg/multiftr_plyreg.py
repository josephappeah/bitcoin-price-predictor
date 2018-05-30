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
reg_param = 0.7  # Regularization Parameter
training_epochs = 20000  # Number of iterations of Gradient Descent
display_step = 1000  # Display Step
testing_days = 30
np.random.seed(0)
random = np.random
p = 9  # Polynomial Power
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

        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            c = S.run(cost)
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \
                "theta=", S.run(theta), "bias=", S.run(bias))

    training_cost = S.run(cost)
    print("Training cost=", training_cost, "theta=", S.run(theta), "bias=", S.run(bias), '\n')

    # Save training results
    plt.plot(Y, 'r', label='Actual Price ($)')
    plt.plot(np.transpose(S.run(hypothesis)), label='Predicted Price ($)')

    plt.title("Training: Multi-Feature Polynomial Regression w/ PCA")
    plt.xlabel("Last 365 Days")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.savefig("P_MultiFtr_PCA_train.png")

    # Save testing results
    hypothesis = tf.matmul(theta, test_X) + bias
    plt.figure(2)
    plt.plot(test_label, 'r', label='Actual Price ($)')
    plt.plot(np.transpose(S.run(hypothesis)), label='Predicted Price ($)')

    plt.title("Testing: Multi-Feature Polynomial Regression w/ PCA")
    plt.xlabel("Following " + str(testing_days) + " Days")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.savefig("P_MultiFtr_PCA_test.png")


    # Print Accuracy
    hypothesis = tf.matmul(theta, train_X) + bias
    accuracy = 1.0 - np.mean((S.run(hypothesis)-train_label)/train_label)
    print(accuracy)


    hypothesis = tf.matmul(theta, test_X) + bias
    #cost = tf.reduce_mean((tf.square(hypothesis - test_label)) / (2 * m))
    #print(S.run(cost))

    '''
    print(test_label)
    print()
    print(S.run(hypothesis))
    '''

    # Save predicted output, and actual output to CSV
    np.savetxt('poly_out', S.run(hypothesis), delimiter='\n')
    np.savetxt('actual_out', test_label, delimiter='\n')

    # Save date
    date = np.array([])
    dates = quandl.get("BCHAIN/MWNUS", returns="numpy")[-testing_days:]

    for day in dates:
        date = np.append(date, day[0].strftime("%m/%d/%Y"))

    print(date)
    #np.savetxt('date_out', date, fmt = '%s', delimiter='\n')
    print(S.run(hypothesis))

    output = np.array([])
    for i in range(len(test_label)):
        val = str(date[i]) + "," + str(test_label[i]) + "," + str(S.run(hypothesis)[0][i])
        output = np.append(output, val)

    np.savetxt('out', output, fmt='%s', delimiter=',')
