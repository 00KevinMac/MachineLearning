def accuracy(self,conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return accuracy. In case of Division by Zero error, return -1.
    [TN, FP, FN, TP] = conf_mat

    acc = 0

    ## YOUR CODE HERE ##

    # To calculate accuracy, we say (TP + TN) / (TP + TN + FN + FP)

    # put 0.0 to make it float
    denominator = 0.0 + TP + TN + FN + FP

    if denominator == 0:
        acc = -1
    else:
        acc = float(TP + TN) / denominator

    return acc


def Q_06(self):
    # Task 6: Please complete the function "accuracy" above
    pass