def F1(self,conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return F1 score. It is the harmonic mean of precision and recall.
    #  In case of Division by Zero error, return -1.

    [TN, FP, FN, TP] = conf_mat

    f1 = 0

    ## YOUR CODE HERE ##

    # The F1 score is: 2TP / (2TP + FP + FN)

    denominator = 2 * TP + FP + FN

    if denominator == 0:
        f1 = -1
    else:
        f1 = (2.0 * TP) / denominator

    return f1


def Q_09(self):
    # Task 9: Please complete the function "F1" above
    pass