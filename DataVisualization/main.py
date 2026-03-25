import os
import sys
from dataset_utils import give_a_colum_name, draw_heatmap
from histogram import visuazlize_histogram
from boxplot import visualize_boxplot
import pandas as pd


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Please give a file path for dataset!\n" \
        "Example usage: python3 main.py ../dataset/data.csv")

    try:
        file_path = sys.argv[1]
        df = pd.read_csv(file_path)
        
        processed_df = give_a_colum_name(df)

        print(processed_df.describe())
        visuazlize_histogram(processed_df)
        visualize_boxplot(processed_df)
        draw_heatmap(processed_df)

    except Exception as e:
        print("Error ocurred:" ,e)