def precision(self,conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return precision. It is also known as Positive Predictive Value (PPV).
    #  In case of Division by Zero error, return -1.
    [TN, FP, FN, TP] = conf_mat


    prec = 0

    ## YOUR CODE HERE

    # Precision is calculated as follows: TP / (TP + FP)

    denominator = 0.0 + TP + FP

    if denominator == 0:
        prec = -1
    else:
        prec = float(TP) / denominator

    return prec


def Q_07(self):
    # Task 7: Please complete the function "precision" above
    pass