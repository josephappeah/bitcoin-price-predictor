"""
Gregory Matthews
Bitcoin: Principal Component Analysis (PCA)
"""
import numpy as np
import matplotlib.pyplot as mplot
import data

# List of Features
features = ["BCHAIN/MWNUS", "BCHAIN/BLCHS", "BCHAIN/MWNTD", "BCHAIN/TRVOU", "BCHAIN/AVBLS", "BCHAIN/NTRBL",
            "BCHAIN/ETRAV", "BCHAIN/NTRAN", "BCHAIN/TRFEE", "BCHAIN/MKTCP", "BCHAIN/TVTVR", "BCHAIN/TRFUS",
            "BCHAIN/HRATE", "CHRIS/ICE_B1", "NASDAQOMX/COMP"]

"""
1.) My Wallet # of users
2.) BlockChain Size
3.) My Wallet # of Trans. Per Day
4.) Exchange Trade Volume
5.) Average BlockChain Size
6.) Number of Transactions per Block
7.) Estimated Transaction Volume
8.) Number of Transactions
9.) Total Transaction Fees
10.) Market Capitalization
11.) Trade Volume vs Transaction Volume Ratio
12.) Total Transaction Fees USD
13.) Bitcoin Hashrate
14.) Crude oil price per day
15.) Nasdaq Composite
"""
n = len(features)
m = 365


# Standard Deviation Function
def standard_dev(X, mean):
    return np.sqrt(np.sum(np.power(X - mean, 2)) / (n - 1.))

# Perform Principle Component Analysis
def pca():

    # Get X data, and standardize
    X = np.zeros([n,m])
    for i, feature in enumerate(features):
        _, X[i, :] = data.get_data(feature, 365)
        mean = np.mean(X[i, :])
        X[i, :] = (X[i, :] - mean) / standard_dev(X[i, :], mean)

    X = X.transpose()

    # Computing Covariance Matrix
    Sigma = np.dot(X.transpose(), X) / (n-1)

    # Computing Eigen Vector/Eigen Values
    val, vect = np.linalg.eigh(Sigma)

    # Determine number of Principle Components, k
    alpha = 0.95
    num = 0
    denom = np.sum(val)
    k = 0
    val_sorted = np.sort(val)[::-1]

    while True:
        num += val_sorted[k]
        if num / denom <= alpha:
            k += 1
        else:
            break


    # Finding k eigenvectors with the largest eigenvalues
    W = np.zeros((n, k))
    picked_ftrs = np.zeros((k))

    for i in range(k):
        picked_ftrs[i] = np.argmax(val)
        W[:, i] = vect[:, np.argmax(val)]
        val[np.argmax(val)] = 0


    # Project D-dimensional data to k-dimensions
    z = np.dot(X, W)

    # Return
    return z

def main():

    z = pca()

    # Compute Principal Components
    PC1 = z[:, 0]
    PC2 = z[:, 1]

    # Plotting
    for i in range(m):
            mplot.scatter([PC1[i]], [PC2[i]], c='b')


    mplot.title('Dimensionality Reduction via PCA')
    mplot.xlabel('PC1')
    mplot.ylabel('PC2')
    mplot.savefig('Bitcoin PCA.png')


if __name__ == "__main__":
    main()
