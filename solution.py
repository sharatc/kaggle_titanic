import utils
import bleach

def main():
    X_train, y_train = utils.read_csv('data/train.csv')
    X_train = bleach.clean_features(X_train)

    print 'X_train shape: %s' % str(X_train.shape)
    print 'y_train shape: %s' % str(y_train.shape)

if __name__ == '__main__':
    main()


