def Q_03(self):
    # Task 3: Return standard deviation of the second feature:"The length of shorter sequence" of
    # the validation dataset: "dataset/validation.csv"
    std = 0

    ## YOUR CODE HERE ##

    #Standard deviation formula is:
    #   1st - work out the mean
    #   2nd - for each number subtract the mean and square the result
    #   3rd - work out the new mean
    #   4th - take the square root of that

    # length = len(self.validation)
    #
    # mean = (self.validation.loc[:,1]).sum() / length
    # newMean = 0
    #
    # for index, row in self.validation.iterrows():
    #     temp = (float(row[1]) - mean)*(float(row[1]) - mean)
    #     newMean += temp
    #
    # mean = newMean / length
    #
    # import math
    # std = math.sqrt(mean)

    # Using builtin function from pandas
    std = self.validation.iloc[:, 1].std()

    return std


