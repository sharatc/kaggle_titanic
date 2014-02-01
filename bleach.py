import numpy as np

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

CLEAN_PCLASS = 0
CLEAN_NAME = 1
CLEAN_SEX = 2
CLEAN_AGE = 3
CLEAN_SIBSP = 4
CLEAN_PARCH = 5
CLEAN_FARE = 6
CLEAN_CABIN = 7
CLEAN_EMBARKED = 8

def clean_features(X):
    """
    Cleans an entire feature vector
    """
    X_clean = []
    for row in X:
        row_clean = [
            row[PCLASS],
            clean_title(row[NAME]),
            clean_sex(row[SEX]),
            clean_age(row[AGE]),
            row[SIBSP],
            row[PARCH],
            row[FARE],
            # note that the ticket column was removed
            clean_cabin(row[CABIN]),
            row[EMBARKED]
        ]
        X_clean.append(row_clean)
    return np.array(X_clean)

def clean_sex(sex):
    return 0 if sex is 'male' else 1

def clean_age(age):
    if not age:
        return 0
    age = float(age)
    if 0.0 <= age < 18.0:
        return 1
    elif 18.0 <= age < 40.0:
        return 2
    else:
        return 3

def clean_title(name):
    for word in name.split():
        if word.endswith('.'):
            title = word
            if title == 'Mr.': title = 1.0
            elif title == 'Miss.': title = 2.0
            elif title == 'Mrs.': title = 3.0
            elif title == 'Master.': title = 4.0
            elif title == 'Dr.': title = 5.0
            else: title = 0
    return title

def clean_cabin(cabin):
    if cabin == 'B' or 'D' or 'E': cabin = 1.0 #80% survival rate
    elif cabin == 'C' or 'F': cabin = 2 #70% survival rate
    elif cabin == '': cabin = 0 #empty cabin
    else: cabin = 3 #50~65% survival rate
    return cabin