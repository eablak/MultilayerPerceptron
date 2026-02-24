import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import statistics
from sklearn.preprocessing import StandardScaler
import numpy as np


def split_df(df):

    df_train, df_valid = train_test_split(df, test_size=0.10, shuffle=True, random_state=42)
    
    X_train = df_train.loc[:, df_train.columns != 'column_1']
    y_train = df_train['column_1'].copy()

    X_valid = df_valid.loc[:, df_valid.columns != 'column_1']
    y_valid = df_valid['column_1'].copy()
    
    le = LabelEncoder()
    y_train = le.fit_transform(y_train)
    y_valid = le.transform(y_valid)

    return X_train, y_train, X_valid, y_valid


def standardize_train(df):

    df_cpy = df.copy()

    mean_vals, std_vals = {}, {}
    for (columnName, columnData) in df_cpy.items():
        mean_val = np.mean(columnData)
        std_val = np.std(columnData)
        df_cpy[columnName] = (columnData - mean_val) / std_val
        mean_vals[columnName] = mean_val
        std_vals[columnName] = std_val

    return df_cpy, mean_vals, std_vals


def standardize_valid(df, mean_vals, std_vals):

    df_cpy = df.copy()

    for (columnName, columnData) in df_cpy.items():
        df_cpy[columnName] = (columnData - mean_vals[columnName]) / std_vals[columnName]
    
    return df_cpy


def save_files(X_train, y_train, X_valid, y_valid):

    X_train = X_train.rename(columns={'column_0':'column_1'})
    X_train.insert(31, "diagnosis", y_train)

    X_valid = X_valid.rename(columns={'column_0':'column_1'})
    X_valid.insert(31, "diagnosis", y_valid)

    output_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/dataset/processed"
    X_train.to_csv(f"{output_dir}/X_train.csv", index=False)
    X_valid.to_csv(f"{output_dir}/X_valid.csv", index=False)


if __name__ == "__main__":

    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    base_path += "/dataset/model_data.csv"
    
    df = pd.read_csv(base_path)

    X_train, y_train, X_valid, y_valid = split_df(df)

    X_train, mean_vals, std_vals  = standardize_train(X_train)
    X_valid = standardize_valid(X_valid, mean_vals, std_vals)

    save_files(X_train, y_train, X_valid, y_valid)