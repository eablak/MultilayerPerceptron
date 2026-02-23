import os
import sys
import pandas as pd

def give_a_colum_name(base_path):

    csv_path = base_path + "/dataset/data.csv"

    try:
        df = pd.read_csv(csv_path)
        df.columns = ["column_"+str(i) for i in range(32)]

        location_path = base_path + "/dataset/model_data.csv"
        df.to_csv(location_path, index=False)
        
        pd.read_csv(location_path)
        
    except Exception as e:
        sys.exit(f"Error: {e}")


def classificate_datas(df, column):
    malignant, benign = [], []
    df = df[['column_1', column]]

    for index, row in df.iterrows():
        if (pd.notna(row[column])):
            if (row['column_1'] == "M"):
                malignant.append(row[column])
            elif (row['column_1'] == "B"):
                benign.append(row[column])

    return malignant, benign
