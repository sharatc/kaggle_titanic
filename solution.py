import numpy as np
import csv

import bleach

PCLASS = 0
NAME = 1
SEX = 2
AGE = 3
SIBSP = 4
PARCH = 5
TICKET = 6
FARE = 7
CABIN = 8
EMBARKED = 9

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

def clean_data(X):
    X_clean = []
    for row in X:
        X_clean.append(X[PCLASS])
        X_clean.append(X[NAME])
        X_clean.append(bleach.clean_sex(X[SEX]))
        X_clean.append(bleach.clean_age(X[AGE]))
        X_clean.append(X[SIBSP])
        X_clean.append(X[PARCH])
        X_clean.append(X[FARE])
        X_clean.append(X[CABIN])
        X_clean.append(X[EMBARKED])
    return X_clean

def main():
    X_train, y_train = read_csv('data/train.csv')

    print 'X_train shape: %s' % str(X_train.shape)
    print 'y_train shape: %s' % str(y_train.shape)

if __name__ == '__main__':
    main()


