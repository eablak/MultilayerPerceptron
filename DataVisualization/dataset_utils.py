import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def give_a_colum_name(df):

    try:
        df.columns = ["column_"+str(i) for i in range(32)]

        df.to_csv("../dataset/model_data.csv", index=False)
        return pd.read_csv("../dataset/model_data.csv")
        
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


def draw_heatmap(df):

    fig, ax = plt.subplots(figsize = (16,8))
    co_mtx = df.corr(numeric_only=True)
    sns.heatmap(co_mtx, annot=True, cmap=plt.get_cmap('coolwarm'))
    ax.set_yticklabels(ax.get_yticklabels(), rotation="horizontal")
    plt.savefig('co_heatmap.png', bbox_inches='tight', pad_inches=0.0)
