import numpy as np


# The function loads data from a text file with a relative path
# 'fname'
# and returns it as a pair of arrays: features
# and diabetes presence.
def read_data(fname):
    # Load data from a CSV file using numpy.genfromtxt.
    data = # TODO
    # The data is split into X (all columns but the last) and
    # y (the last column).
    X, y = data[:, :-1], data[:, -1]
    # Standardize features: subtract the mean
    # and divide by the standard deviation for each column.
    X = # TODO
    # Prepend a column of -1s to X.
    # It acts as a pseudo-feature that simplifies our vector
    # calculations later on.
    X = # TODO
    # Map labels from {0,1} to {1,-1}.
    y =  # TODO
    return X, y


if __name__ == '__main__':
    X, y = read_data("pima-indians-diabetes.csv")
    print(f'Features in X array:', X)
    print(f'Diabetes: ', y)
