def Q_15(self):
    # Task 15: Scale the all the features of the validaton set using the formula, z = (x-m)/s,
    #   where m = mean of a feature in the training set: "dataset/training.csv"
    #         s = standard deviation of the feature in the training set: "dataset/training.csv"
    #  DO NOT SCALE the target feature.
    # At the end, return a tuple (X, y), with X being a numpy array of shape (N,8) and y is an N dim array
    # and N is the total number of samples in the validation set: "dataset/validation.csv".

    X = None
    y = None


    ## YOUR CODE HERE ##

    y = self.validation.iloc[:, -1].values

    m = self.training.iloc[:, 0:-1].mean()
    s = self.training.iloc[:, 0:-1].std()

    X = self.validation.iloc[:, 0:-1].sub(m)
    X = X.div(s)

    X = X.values

    return (X, y)
