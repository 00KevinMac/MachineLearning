def Q_17(self, judge_dataset):
    # Task 17: Utilizing the best trained linear regression model (so far), predict the target for each
    # of the samples in the judge_dataset.
    # I believe you will not forget to scale the input variables based on the same metrics you used to scale
    # the training dataset. If you did not save those metrics, you may need to recompute again(!)
    # Return a vector, y_pred, as a  numpy array the predicted target values.
    # PLEASE DO NOT USE ANY LIBRARY FUNCTION THAT DOES THE LINEAR REGRESSION.
    import numpy as np

    y_pred = np.array([])

    ## YOUR CODE HERE ##

    # --- The training data ---
    # One hot encoding
    one_hot_dataset = self.Q_02(self.full_dataset)

    # Find any missing values and fill them with the mean
    missing_count, revised_full_dataset = self.Q_03(one_hot_dataset)

    # Get the correlation set (for top 20 columns)
    corr_dataset = self.Q_04(one_hot_dataset)

    # Return dataset with those top 20 columns and append BWEIGHT
    reduced_full_dataset = self.Q_05(revised_full_dataset, corr_dataset)

    # Split into features and target
    X, y = self.Q_06(reduced_full_dataset)

    # Split into training and test data
    X_train, X_test, y_train, y_test = self.Q_07(X, y)


    # --- The test data ---
    # One hot encoding
    one_hot_dataset = self.Q_02(judge_dataset)

    # Find any missing values and fill them with the mean
    missing_count, revised_full_dataset_test = self.Q_03(one_hot_dataset)

    # Return the dataset with the top 20 correlated values (calculated earlier)
    reduced_full_dataset_test = revised_full_dataset_test[corr_dataset['variable_name']]


    # --- Scale all the data the same way ---
    X_train, X_test_judge, y_train, y_test = self.Q_09(X_train, reduced_full_dataset_test, y_train, y_test)


    # --- To do the actual prediction on the Judge Dataset ---
    # minibatch = self.Q_13(X_train, X_test_judge, y_train, y_test)
    # beta, y_pred, RMSE, cpu_time = minibatch

    beta, y_pred, RMSE = self.Q_10(X_train, X_test_judge, y_train, y_test)


    return y_pred