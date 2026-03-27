import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import statistics
from sklearn.preprocessing import StandardScaler
import numpy as np
import json


def give_a_colum_name(df):

    try:
        if all([item in df.columns for item in ["column_"+str(i) for i in range(32)]]):
            return df

        df.columns = ["column_"+str(i) for i in range(32)]
        df.to_csv("../../dataset/model_data.csv", index=False)
        
        return pd.read_csv("../../dataset/model_data.csv")
        
    except Exception as e:
        sys.exit(f"Error: {e}")


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

    output_dir = "../../dataset/processed"

    X_train.to_csv(f"{output_dir}/X_train.csv", index=False, header=False)
    X_valid.to_csv(f"{output_dir}/X_valid.csv", index=False, header=False)
    
    pd.DataFrame(y_train).to_csv(f"{output_dir}/y_train.csv", index=False, header=False)
    pd.DataFrame(y_valid).to_csv(f"{output_dir}/y_valid.csv", index=False, header=False)


def save_statistics(mean_vals, std_vals):
    
    parameters = {"mean_vals": mean_vals, "std_vals": std_vals}
    json_str = json.dumps(parameters)

    with open("statistics.json", "w") as f:
        f.write(json_str)



if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Please give a file path for dataset!\n" \
        "Example usage: python3 preprocessing.py ../../dataset/data.csv")

    try:
        file_path = sys.argv[1]
        df = pd.read_csv(file_path)

        processed_df = give_a_colum_name(df)

        X_train, y_train, X_valid, y_valid = split_df(processed_df)

        X_train, mean_vals, std_vals  = standardize_train(X_train)
        X_valid = standardize_valid(X_valid, mean_vals, std_vals)

        # save_statistics(mean_vals, std_vals)
        save_files(X_train, y_train, X_valid, y_valid)

    except Exception as e:
        print("Error occured:" ,e)