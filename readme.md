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


<b>If you will run evaluation.py file you will get data_training.csv and data_test.csv files. You can run your train.py with data_training.csv after get model.npy file use it on your data_test.csv file and get the results.</b>