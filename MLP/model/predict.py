import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import numpy as np
from model.train import MLP
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from preprocessing.preprocessing import standardize_train


def predict_preprocessing(df):

    df.columns = ["column_"+str(i) for i in range(32)]

    X = df.loc[:, df.columns != 'column_1']
    y = df['column_1'].copy()

    le = LabelEncoder()
    y = le.fit_transform(y)
    y = np.eye(2)[y.astype(int).flatten()].T 

    X, _, _  = standardize_train(X)

    return X, y


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Please give a file path for dataset!\n" \
        "Example usage: python3 predict.py ../../dataset/data_test.csv")
    
    try:
        file_path = sys.argv[1]
        df = pd.read_csv(file_path)
        
        X, y = predict_preprocessing(df)

        mlp = MLP()
        model = mlp.load_model()

        layer_dims = model["layer_dims"]
        parameters = model["parameters"]
        activation = model["activation"]

        predictions, _ = mlp.forward_propagation(X.T, parameters=parameters, activation=activation)
        loss = mlp.cost_function(predictions, y)

        predictions_class = np.argmax(predictions, axis=0)
        accuracy = np.sum(predictions_class == y) / len(y)
        
        print(f"Accuracy: {accuracy:.2f}")
        print(f"Loss: {loss:.2f}")

    except Exception as e:
        print("Error ocurred:" ,e)