def Q_02(self):
    #Task 2: Return a list of of two numbers: [n0, n1], where
    # n0 represents number of class=0 (negative) samples and n1 represents number of class=1 (positive) samples
    # in the validation dataset: "dataset/validation.csv"
    n0 = 0
    n1 = 0

    ## YOUR CODE HERE ##

    n0 = (self.validation.iloc[:,self.target_column] == 0).sum()
    n1 = (self.validation.iloc[:,self.target_column] == 1).sum()

    return [n0, n1]