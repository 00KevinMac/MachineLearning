def Q_02(self, full_dataset):
    #Task 2: Takes full_dataset (Pandas dataframe) as input,
    # and returns a revised full_dataset Dataframe after replacing all the non-numeric variables (i.e.,
    # categorical variables) with numeric encoding. Please consider using the "One-hot encoding" scheme
    # i.e., introducing dummy variables. A brief description of the scheme can be found in the READMEs/DUMMY-variables.note.txt
    # file
    import pandas as pd

    ## YOUR CODE HERE ##

    # Dataframe to return eventually
    return_df = full_dataset

    # Get the columns that are char or string
    temp_df = full_dataset.select_dtypes(exclude='number')

    # Get the names of those columns
    selected_columns = list(temp_df.columns)

    # One hot encode and add the resulting columns to the original dataframe
    return_df = pd.concat([return_df, pd.get_dummies(return_df[selected_columns])], axis=1)

    # drop original columns
    return_df.drop(selected_columns, axis=1, inplace=True)



    return return_df