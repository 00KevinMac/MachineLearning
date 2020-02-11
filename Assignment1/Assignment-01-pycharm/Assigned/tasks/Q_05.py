def confusion_matrix(self,y_actual, y_pred):
    # Task 5: the function takes two arrays of target variable "y": y_actual and y_pred
    #    denoting ground truth class labels and predicted class labels for the N samples
    #    when N is the length of both the arrays.
    # The function should return a list of 4 metrics: TN, FP, FN, TP (in this order).
    assert(len(y_actual) == len(y_pred))

    TP = 0
    FP = 0
    TN = 0
    FN = 0

    ## YOUR CODE HERE ##
    for i in range(len(y_actual)):
        if (y_actual[i] == 1):

            # True Positive
            if (y_actual[i] == y_pred[i]):
                TP += 1
            else:
                # False Negative
                FN += 1
        elif (y_actual[i] == 0):

            # True Negative
            if(y_actual[i] == y_pred[i]):
                TN += 1
            else:
                # False Positive
                FP += 1

    return [TN, FP, FN, TP]


# def confusion_matrix(self,TP, TN, FP, FN):
#     return [TN, FP, FN, TP]


def Q_05(self):
    # Task 5: This function does nothing, but you need to complete the two functions "confusion_matrix" above
    #   First "confusion_matrix" takes two arguments: y_actual and y_pred
    # And the second overloaded version of the function takes 4 arguments: TP, TN, FP, FN
    pass


