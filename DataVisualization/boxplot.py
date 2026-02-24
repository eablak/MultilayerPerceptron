import matplotlib.pyplot as plt
import pandas as pd
from dataset_utils import classificate_datas


def visualize_boxplot(df):

    fig = plt.figure(figsize=(10,7))
    columns = ["column_"+str(i) for i in range(32)]

    for column in columns:
        if column == "column_1":
            continue
        malignant, benign = classificate_datas(df, column)
        
        plt.boxplot([malignant, benign], tick_labels=["malignant", "benign"])
        plt.title(column)
        
        plt.show()

    """
        Results: 
        less seperator columns are:
            (median's close to eachother & narrow IQR & Overlap)
            columns = ["column_0", "column_10", "column_11", "column_13", "column_16", "column_18", "column_20", "column_21"]
        most seperators:
            columns = ["column_2", "column_4", "column_5", "column_22", "column_24", "column_25", "column_28", "column_29", ]
    """