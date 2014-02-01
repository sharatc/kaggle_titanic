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
        X_clean.append(clean_title(row[NAME]))
        X_clean.append(clean_sex(row[SEX]))
        X_clean.append(clean_age(row[AGE]))
        X_clean.append(row[SIBSP])
        X_clean.append(row[PARCH])
        X_clean.append(row[FARE])
        # note that the ticket column was removed
        X_clean.append(clean_cabin(row[CABIN]))
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