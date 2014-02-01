import numpy as np
import csv

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
