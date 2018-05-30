import numpy as np
import matplotlib.pyplot as plt

# Initialize arrays
Y, poly_pred, lstm_pred = np.array([]), np.array([]), np.array([])

# Initial value for backtesting
USD = 10000.00  # Monetary amount used for testing
BTC = 0.00  # Number of Bitcoins to purchase
pred_threshold = 0.99  # Threshold for determining when to buy/sell
sentiment_threshold = 1.00 # Threshold for sentiment analysis
returns = np.array([10000.])
bought, sold = 0, 0  # How many times Bitcoin has been bought/sold

# Initialize constants
POLY_ACCURACY = 0.8792
LSTM_ACCURACY = 0.9836


def ensemble_avg(poly_pred, lstm_pred):
    """
    Ensemble Averaging algorithm: weighted voting based on training accuracy
    inputs: Polynomial Reg prediction, RNN with LSTM prediction
    output: Final weighted average prediction
    """
    poly_weight = POLY_ACCURACY/(LSTM_ACCURACY+POLY_ACCURACY)
    lstm_weight = LSTM_ACCURACY/(LSTM_ACCURACY+POLY_ACCURACY)

    # Make sure corresponding weights are correct
    assert poly_weight + lstm_weight == 1

    return poly_weight*poly_pred + lstm_weight*lstm_pred

# Extract Polynomial Regression prediction and add to array
with open('poly_NEXTDAY', 'r') as f:
    for line in f:
        pred = line.replace('\r', ',').split(',')
        Y = np.append(Y, float(pred[1]))
        poly_pred = np.append(poly_pred, float(pred[2]))


# Extract RNN with LSTM prediction and add to array
with open('lstm_NEXTDAY', 'r') as f:
    for line in f:
        pred = line.replace('\n', '').split(',')
        lstm_pred = np.append(lstm_pred, float(pred[2]))

final = np.array([])
final = np.append(final, ensemble_avg(poly_pred[0], lstm_pred[0]))
np.savetxt('ensemble_NEXTDAY', final)
