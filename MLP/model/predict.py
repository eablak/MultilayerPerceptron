import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import numpy as np
from model.train import MLP
import pandas as pd
from DataVisualization.dataset_utils import give_a_colum_name





if __name__ == "__main__":
    
    mlp = MLP()

    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    base_path += "/dataset/processed/"

    df = pd.read_csv(base_path)

    parameters = mlp.load_parameters()