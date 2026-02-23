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
        Most Outliers
            Seperated Good:
            column_9, column_27, column_28
            Normal Seperated:
            column_3, column_14, column_17, column_19, column_31
            
            Seperated Not Good:
            column__11, column_15, column_16, column_18, column_20, column_21
    """