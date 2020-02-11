def FDR(self,conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return False Discovery Rate (FDR).
    #  In case of Division by Zero error, return -1.
    [TN, FP, FN, TP] = conf_mat
    fdr = 0

    ## YOUR CODE HERE ###

    # False Discovery Rate is:
    # FDR = FP / (FP + TP)

    denominator = 0.0 + FP + TP

    if denominator == 0:
        fdr = -1
    else:
        fdr = float(FP) / denominator

    return fdr


def Q_11(self):
    # Task 11: Please complete the function "FDR" above
    pass