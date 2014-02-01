import numpy as np
import csv

import bleach

def read_csv(filename):
    """
    Reads a CSV file by filename and returns the numpy
    array of the features and targets.
    """
    reader = csv.reader(open(filename, 'rb'))

    # remove the headers
    reader.next()

    X = []
    y = []
    for row in reader:
        X.append(row[2:])
        y.append(row[1])
    return np.array(X), np.array(y)

def main():
    X_train, y_train = read_csv('data/train.csv')
    X_train = bleach.clean_features(X_train)

    print 'X_train shape: %s' % str(X_train.shape)
    print 'y_train shape: %s' % str(y_train.shape)

if __name__ == '__main__':
    main()


