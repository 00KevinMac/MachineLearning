def Q_12(self, model_files=["models/Model_1.pkl","models/Model_2.pkl","models/Model_3.pkl",\
                            "models/Model_4.pkl","models/Model_5.pkl","models/Model_6.pkl"]):
    # Task 12: Return as a dataframe containing:
    # {model_name,acc,prec,rec,f1,mcc,FDR} for each of the N models (listed in model_files)
    # predicting the target variables  of the validation data: "dataset/validation.csv"
    # You can load the pretrained model via pickle library. Here is an example use:
    # infile = open('pickle-file.pkl','rb')
    # model = pickle.load(infile)
    # infile.close()
    # y_pred = model.predict(X) #to get the predictions of all the X samples using the model
    import pickle
    import numpy as np
    import pandas as pd
    import sys
    import os
    from sklearn.linear_model import LogisticRegression
    from sklearn.neural_network import MLPClassifier
    from sklearn import tree
    from sklearn.svm import SVC
    from sklearn.neighbors import KNeighborsClassifier
    result = pd.DataFrame(columns=['model_name','Accuracy','Precision','Recall','F1','MCC','FDR'])


    ## YOUR CODE HERE ##

    for fileIndex in range(len(model_files)):
        infile = open(model_files[fileIndex], 'rb')
        model = pickle.load(infile)
        infile.close()

        y_pred = model.predict(self.validation.iloc[:, 0:-1])
        y_actual = self.validation.iloc[:, -1]

        confusion_matrix = self.confusion_matrix(y_actual, y_pred)

        result.loc[fileIndex] = [model_files[fileIndex], self.accuracy(confusion_matrix), self.precision(confusion_matrix),
                         self.recall(confusion_matrix), self.F1(confusion_matrix), self.MCC(confusion_matrix),
                         self.FDR(confusion_matrix)]

    return result