import os
import sys
import pandas as pd

def give_a_colum_name(base_path):

    csv_path = base_path + "/dataset/data.csv"

    try:
        df = pd.read_csv(csv_path)
        df.columns = ["column_"+str(i) for i in range(32)]

        # print(df)
        location_path = base_path + "/dataset/model_data.csv"
        df.to_csv(location_path, index=False)
        
        new_df = pd.read_csv(location_path)
        print(new_df)
        
    except Exception as e:
        sys.exit(f"Error: {e}")


if __name__ == "__main__":
    
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    give_a_colum_name(base_path)