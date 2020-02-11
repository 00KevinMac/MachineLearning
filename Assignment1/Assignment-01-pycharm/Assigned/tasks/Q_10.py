def MCC(self,conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return Matthews correlation coefficient (MCC).
    #  In case of Division by Zero error, return -1.
    [TN, FP, FN, TP] = conf_mat
    mcc = 0

    ## YOUR CODE HERE ##

    # MCC can be calculated as follows:
    # MCC = (TP * TN - FP * FN) / sqrt[ (TP+FP)(TP+FN)(TN+FP)(TN+FN) ]

    # import math

    denominator = 0.0 + ((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))**0.5  # math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))

    if denominator == 0:
        mcc = -1
    else:
        mcc = float(TP * TN - FP * FN) / denominator

    return mcc


def Q_10(self):
    # Task 10: Please complete the function "MCC" above
    pass