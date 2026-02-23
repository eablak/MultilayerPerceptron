import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import sys

def draw_histogram_overlay(malignant, benign, column):

    plt.hist(malignant, bins=25, alpha=0.45, color='green')
    plt.hist(benign, bins=25, alpha=0.45, color='red')

    plt.title(column)
    plt.legend(['malignant', 'benign'])

    plt.show()


def draw_histogram_seperate(malignant, benign, column):

    plt.subplot(1,2,1)
    plt.title("Malignant")
    plt.hist(malignant)

    plt.subplot(1,2,2)
    plt.title("Benign")
    plt.hist(benign)

    plt.suptitle(column)
    plt.show()

def histogram_datas(df, column):

    malignant, benign = [], []
    df = df[['column_1', column]]

    for index, row in df.iterrows():
        if (pd.notna(row[column])):
            if (row['column_1'] == "M"):
                malignant.append(row[column])
            elif (row['column_1'] == "B"):
                benign.append(row[column])

    return malignant, benign


if __name__ == "__main__":

    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_path += "/dataset/model_data.csv"

    try:
        df = pd.read_csv(base_path)
        columns = ["column_"+str(i) for i in range(32)]
        for column in columns:
            if column == "column_1":
                continue
            malignant, benign = histogram_datas(df, column)
            draw_histogram_seperate(malignant, benign, column)
            draw_histogram_overlay(malignant, benign, column)

        """
        less seperator columns are: 
            columns = ["column_0", "column_6", "column_13", "column_16", "column_18", "column_19", "column_20", "column_21"]
        most seperators:
            columns = ["column_2", "column_4", "column_8", "column_9", "column_22", "column24", "column25"]
        column_5 outliers?
        """
    except Exception as e:
        sys.exit(f"Error: {e}")