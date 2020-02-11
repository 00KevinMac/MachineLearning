def Q_19(self, model_file="models/Model_1.pkl"):
    # Task 19: Flip the prediction of Model 1, and then compute and
    #  return as a dataframe containing:
    #      {acc,prec,rec,f1,mcc,FDR} on the
    #   original (i.e., not-scaled) validation dataset: "dataset/validation.csv"
    #     # You can load the pretrained model via pickle library. Here is an example use:
    #     # infile = open('pickle-file.pkl','rb')
    #     # model = pickle.load(infile)
    #     # infile.close()
    #     # y_pred = model.predict(X) #to get the predictions of all the X samples using the model
    import pickle
    import sys
    import os
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LogisticRegression
    from sklearn.neural_network import MLPClassifier
    from sklearn import tree
    from sklearn.svm import SVC
    from sklearn.neighbors import KNeighborsClassifier

    acc = 0
    prec = 0
    rec = 0
    f1 = 0
    mcc = 0
    fdr = 0

    ## YOUR CODE HERE ##

    infile = open(model_file,'rb')
    model = pickle.load(infile)
    infile.close()

    y_pred = model.predict(self.validation.iloc[:, 0:-1])
    y_predFlipped = np.logical_xor(y_pred, 1).astype(int)
    y_actual = self.validation.iloc[:, -1]

    confusion_matrix = self.confusion_matrix(y_actual, y_predFlipped)

    acc = self.accuracy(confusion_matrix)
    prec = self.precision(confusion_matrix)
    rec = self.recall(confusion_matrix)
    f1 = self.F1(confusion_matrix)
    mcc = self.MCC(confusion_matrix)
    fdr = self.FDR(confusion_matrix)

    result = pd.DataFrame({'Accuracy':[acc],'Precision':[prec],'Recall':[rec],\
                           'F1':[f1],'MCC':[mcc],'FDR':[fdr]})
    return result