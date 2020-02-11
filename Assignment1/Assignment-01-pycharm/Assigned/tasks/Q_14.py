def Q_14(self, performance_result_dataframe):
    # Task 14: Return the model name with path which is performing the worst in terms of recall, given the
    #  performance result dataframe from Q_12
    name = "models/YYYYYY.pkl"

    ## YOUR CODE HERE ##

    row = performance_result_dataframe.iloc[:, 3].idxmin()
    name = performance_result_dataframe.iloc[row, 0]

    return name