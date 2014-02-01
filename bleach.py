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

def clean_features(X):
    """
    Cleans an entire feature vector
    """
    X_clean = []
    for row in X:
        X_clean.append(row[PCLASS])
        X_clean.append(row[NAME])
        X_clean.append(clean_sex(row[SEX]))
        X_clean.append(clean_age(row[AGE]))
        X_clean.append(row[SIBSP])
        X_clean.append(row[PARCH])
        X_clean.append(row[FARE])
        # note that the ticket column was removed
        X_clean.append(row[CABIN])
        X_clean.append(row[EMBARKED])
    return X_clean

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
