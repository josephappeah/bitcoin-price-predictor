import numpy as np
import matplotlib.pyplot as plt

# Initialize arrays
Y, poly_pred, lstm_pred = np.array([]), np.array([]), np.array([])
sentiment_pred, sentiment_grad_pred = np.array([]), np.array([])

# Initial value for backtesting
USD = 10000.00  # Monetary amount used for testing
BTC = 0.00  # Number of Bitcoins to purchase
pred_threshold = 1.00  # Threshold for determining when to buy/sell
sentiment_threshold = 1.000 # Threshold for sentiment analysis
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


# Extract actual market price of Bitcoin and add to array
with open('actual_out', 'r') as f:
    for line in f:
        for val in line.split():
            Y = np.append(Y, float(val))

# Extract polynomial regression prediction and add to array
with open('poly_out', 'r') as f:
    for line in f:
        for pred in line.split():
            poly_pred = np.append(poly_pred, float(pred))

# Extract RNN with LSTM prediction and add to array
with open('lstm_out', 'r') as f:
    for line in f:
        pred = line.replace('\n', '').split(',')
        lstm_pred = np.append(lstm_pred, float(pred[2]))

# Extract Sentiment Analysis and add to array
with open('sentiment_out', 'r') as f:
    line = f.readline().replace('\r', ',').split(',')
    for pred in line[1::3]:
        sentiment_pred = np.append(sentiment_pred, float(pred))
    for pred in line[2::3]:
        sentiment_grad_pred = np.append(sentiment_grad_pred, float(pred))

print("Starting Amount: $%.2f" % USD)

# Back-testing Algorithm - Trading Strategy
for i in range(Y.shape[0]-1):

    # Perform ensemble learning
    prediction = ensemble_avg(poly_pred[i+1], lstm_pred[i+1])

    # Predict price increase - BUY
    if USD is not 0.0 and prediction > Y[i]*pred_threshold \
            and (sentiment_pred[i+1] > 0.5*sentiment_threshold and sentiment_grad_pred[i+1] > 0.0*sentiment_threshold):
        BTC = USD / Y[i]
        USD = 0.0
        print("Bought BTC at $%.2f" % Y[i])
        bought += 1

    # Predict price decrease - SELL
    elif (BTC is not 0.0 and prediction < Y[i]/pred_threshold) \
            and (sentiment_pred[i+1] < 0.5/sentiment_threshold or sentiment_grad_pred[i+1] < 0.0*sentiment_threshold):
        USD = Y[i] * BTC
        BTC = 0.0
        print("Sold BTC at $%.2f" % Y[i])
        print("New Amount: $%.2f" % USD)
        sold += 1

    # Save value to return array
    if BTC is 0.0:
        returns = np.append(returns, USD)
    else:
        returns = np.append(returns, Y[i] * BTC)

# Print final return
if BTC is 0.0:
    print("Final Amount: $%.2f" % USD)
else:
    print("Final Amount: $%.2f" % (BTC*Y[-1]))
print("Bought: %d\nSold: %d" % (bought, sold))


def main():

    # Plot prediction against results
    plt.plot(Y, 'r', label='Actual Price ($)', linewidth=1.5)
    plt.plot(poly_pred, label='Polynomial Regression Prediction ($)', linewidth =1.0)
    plt.plot(lstm_pred, label='RNN with LSTM Prediction ($)', linewidth=1.0)
    plt.plot(ensemble_avg(poly_pred, lstm_pred), label = 'Ensemble Learning', linewidth=1.5)
    plt.title("Supervised ML model predictions of Bitcoin Market Price")
    plt.xlabel("Last Month")
    plt.ylabel("Price ($)")
    plt.legend(prop={'size': 6})
    plt.savefig("PolyReg_LSTM_Plot.png")

    # Plot returns
    plt.figure(2)
    plt.plot(returns/10000., label='Trading Agent')
    plt.title("Simulated Bitcoin Trading: Percent Returns")
    plt.xlabel("Day")
    plt.ylabel("Return (%)")
    plt.legend()
    plt.savefig("Percent Returns.png")


if __name__ == "__main__":
    main()

