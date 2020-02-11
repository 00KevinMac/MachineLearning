def recall(self,conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return recall. It is also known as Sensitivity, or True Positive Rate (TPR).
    #  In case of Division by Zero error, return -1.
    [TN, FP, FN, TP] = conf_mat

    rec = 0

    ## YOUR CODE HERE ##

    # To calculate recall: TP / (TP + FN)

    denominator = 0.0 + TP + FN

    if denominator == 0:
        rec = -1
    else:
        rec = float(TP) / denominator

    return rec


def Q_08(self):
    # Task 8: Please complete the function "recall" above
    pass