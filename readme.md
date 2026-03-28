# Project structure

## Project Requirements

If you don't have create dataset/processed folders on your project main path to not get directory errors. And add data.csv and evaluation.py file in datset folder from project_requirements folder.

## DataVisualization

This part for IV.2 Dataset. The aim for here exploring the dataset, displaying it with graphs and visualizing. We will get:

- dataset descriptions
- histogram visualization
- boxplot visualization
- heatmap correlation

for detailly information check [this.](DataVisualization/reamdme.md)

## MLP

### preprocessing

In here we will separate dataset into two parts: one for training and one for validation. Result files are X_train, y_train, X_valid, y_valid.

The data is raw and should be preprocessed before being used for the training phase. For this one we will standardize x_train dataset with X_train values. After find the mean_vals and std_vals via x_train dataset we will use this values also for standardize x_valid dataset. The point for standardize x_valid with x_train values to <b>prevent dataleak</b> on x_valid dataset.

### model/train

All neural network implementation and training process handled in here. And detailly information explained in [readme_files](MLP/model/readme/) step by step.

### model/predict

After train process finished training results will be saved on model.npy file. This will allow us to use same model on different datasets. Run the prediction program and see model's performance via validation dataset.


### If you want to evaluate model:
1) Put evaluation.py and data.csv file under dataset folder
2) After runing evaluation.py file you will get data_training.csv and data_test.csv
3) To be able to train you model with data_training.csv you need to preprocess it. Run the preprocessing.py file with data_training.csv file. After this processing step you will get X_train, X_valid, y_train, y_valid files under dataset/processed folder.
4) Run the train.py file it will use your files under dataset/processed. After training process finish model will be saved on model.npy file.
5) Test your model accuracy with prediction.py file. Run the prediction.py file with data_test.csv file and get the results.
6) You can train and predict many times and every time accuracy and loss will be different. With this parameters loss is under 0.08 If you want you can update parameters and change model structure.
