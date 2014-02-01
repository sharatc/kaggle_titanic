import numpy as np
import matplotlib.pyplot as plt

import utils
import bleach

def analyze_fare(X):
    plt.figure(1)
    plt.title('Fare Histogram')
    plt.xlabel('Bins')
    plt.ylabel('Fare')
    plt.hist(X[:, bleach.CLEAN_FARE].astype(np.float), bins=range(0, 100, 10))
    plt.show()

def main():
    X_train, y_train = utils.read_train_csv('data/train.csv')
    X_train = bleach.clean_features(X_train)

    analyze_fare(X_train, y_train)

if __name__ == '__main__':
    main()
