import os
import sys
from dataset_utils import give_a_colum_name
from histogram import visuazlize_histogram
from boxplot import visualize_boxplot
import pandas as pd


if __name__ == "__main__":
    
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    give_a_colum_name(base_path)

    base_path += "/dataset/model_data.csv"
    df = pd.read_csv(base_path)

    # print(df.describe())
    # visuazlize_histogram(df)
    visualize_boxplot(df)
    