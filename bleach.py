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

