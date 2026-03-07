import numpy as np
import os
import argparse
import matplotlib.pyplot as plt

class MLP:

    def get_dataset(self):
        
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        base_path += "/dataset/processed/"

        X_train = np.loadtxt(base_path+"X_train.csv", delimiter=",")
        X_train = X_train.T
        y_train = np.loadtxt(base_path+"y_train.csv", delimiter=",").reshape(1, X_train.shape[1])
        y_train = np.eye(2)[y_train.astype(int).flatten()].T 
        
        X_valid = np.loadtxt(base_path+"X_valid.csv", delimiter=",")
        X_valid = X_valid.T
        y_valid = np.loadtxt(base_path+"y_valid.csv", delimiter=",").reshape(1, X_valid.shape[1])
        y_valid = np.eye(2)[y_valid.astype(int).flatten()].T 

        # print(X_train.shape)

        return X_train, y_train, X_valid, y_valid
    

    # ACTIVATION FUNCTIONS

    def sigmoid(self, Z):
        A = 1/(1+np.exp(-Z))
        return A
    

    def softmax(self, z):
        z = z - np.max(z, axis=0, keepdims=True)
        expZ = np.exp(z)
        return expZ/(np.sum(expZ, axis=0, keepdims=True))
    

    def relu(self, Z):
        A = np.maximum(0, Z)
        return A
    

    def tanh(self, x):
        return np.tanh(x)
    

    def derivative_relu(self, x):
        return np.array(x > 0, dtype='float')
    

    def derivative_tanh(self, x):
        return (1 - np.power(x, 2))
    

    # Step1: Initialize Parameters
    def initialize_parameters(self, layer_dims):

        L = len(layer_dims) - 1
        parameters = {}

        for l in range(1, L+1):
            parameters["W" + str(l)] = np.random.randn(layer_dims[l], layer_dims[l-1]) / np.sqrt(layer_dims[l-1])
            parameters["b" + str(l)] = np.zeros((layer_dims[l], 1))

        return parameters


    def tester_initialize_parameters(self):

        X_train, y_train, X_valid, y_valid = self.get_dataset()
        layer_dims = [X_train.shape[0], 16, 8, y_train.shape[0]]
        params = self.initialize_parameters(layer_dims)

        for l in range(1, len(layer_dims)):
            print("Shape of W" + str(l) + ": ", params['W'+str(l)].shape)
            print("Shape of b" + str(l) + ": ", params['b'+str(l)].shape, "\n")


    # Step2: Forward Propagations
    def forward_propagation(self, X, parameters, activation="relu"):

        forward_cache = {}
        L = len(parameters) // 2
        forward_cache["A0"] = X

        for l in range(1, L):
            forward_cache['Z' + str(l)] = parameters['W' + str(l)].dot(forward_cache['A' + str(l-1)]) + parameters['b' + str(l)]
            if activation == 'relu':
                forward_cache['A' + str(l)] = self.relu(forward_cache['Z' + str(l)])
            else:
                forward_cache['A' + str(l)] = self.tanh(forward_cache['Z' + str(l)])


        forward_cache['Z' + str(L)] =  parameters['W' + str(L)].dot(forward_cache['A' + str(L-1)]) + parameters['b' + str(L)]
        forward_cache['A' + str(L)] = self.softmax(forward_cache['Z' + str(L)])

        return forward_cache['A' + str(L)], forward_cache
    

    def tester_forward_propagation(self):

        X_train, y_train, X_valid, y_valid = self.get_dataset()
        layer_dims = [X_train.shape[0], 16, 8, y_train.shape[0]]
        params = self.initialize_parameters(layer_dims)
        aL, forw_cache = self.forward_propagation(X_train, params, 'relu')

        for l in range(len(params)//2 + 1):
            print("Shape of A" + str(l) + ": ", forw_cache['A' + str(l)].shape)


    # Step3: Cost Function
    def cost_function(self, AL, Y):

        m = Y.shape[1]

        cost = - (1./m) * np.sum(Y*np.log(AL))
        cost = np.squeeze(cost)

        return cost
    

    # Step4: Back Propagation
    def backward_propagation(self, AL, Y, parameters, forward_cache, activation):

        grads = {}
        L = len(parameters)//2
        m = Y.shape[1]

        grads["dZ" + str(L)] = AL - Y
        grads["dW" + str(L)] = (1./m) * np.dot(grads['dZ' + str(L)], forward_cache["A" + str(L-1)].T)
        grads["db" + str(L)] = (1./m) * np.sum(grads['dZ' + str(L)], axis=1, keepdims=True)

        for l in reversed(range(1, L)):
            if activation == "relu":
                grads["dZ" + str(l)] = np.dot(parameters['W' + str(l+1)].T, grads["dZ" + str(l+1)]) * self.derivative_relu(forward_cache['A' + str(l)])
            else:
                grads["dZ" + str(l)] = np.dot(parameters['W' + str(l+1)].T, grads["dZ" + str(l+1)]) * self.derivative_tanh(forward_cache['A' + str(l)])

            grads["dW" + str(l)] = (1./m) * np.dot(grads["dZ" + str(l)], forward_cache["A" + str(l-1)].T)
            grads["db" + str(l)] = (1./m) * np.sum(grads["dZ" + str(l)], axis=1, keepdims=True)

        return grads


    def tester_backword_propagation(self):
        
        X_train, y_train, X_valid, y_valid = self.get_dataset()
        layer_dims = [X_train.shape[0], 16, 8, y_train.shape[0]]
        params = self.initialize_parameters(layer_dims)
        aL, forw_cache = self.forward_propagation(X_train, params, 'relu')
        grads = self.backward_propagation(forw_cache["A" + str(3)], y_train, params, forw_cache, "relu")

        for l in reversed(range(1, len(grads)//3 + 1)):
            print("Shape of dZ" + str(l) + ": ", grads['dZ' + str(l)].shape)
            print("Shape of dW" + str(l) + ": ", grads['dW' + str(l)].shape)
            print("Shape of db" + str(l) + ": ", grads['db' + str(l)].shape, "\n")

    
    # Step5: Update Parameters
    def update_parameters(self, parameters, grads, learning_rate):
        
        L = len(parameters)//2

        for l in range(1, L+1):
            parameters['W' + str(l)] = parameters['W' + str(l)] - learning_rate*grads['dW' + str(l)]
            parameters['b' + str(l)] = parameters['b' + str(l)] - learning_rate*grads['db' + str(l)]

        return parameters
    
    
    def model(self, X_train, y_train, X_valid, y_valid, layer_dims, learning_rate, activation="relu", epochs=100):

        parameters = self.initialize_parameters(layer_dims)
        history = {"epoch": [], "accuracy": [], "loss": [], "val_accuracy": [], "val_loss": []}

        for i in range(0, epochs):

            AL, forward_cache = self.forward_propagation(X_train, parameters, activation)
            cost = self.cost_function(AL, y_train)
            grads = self.backward_propagation(AL, y_train, parameters, forward_cache, activation)
            parameters = self.update_parameters(parameters, grads, learning_rate)
            
            AL_valid, forward_cache_valid = self.forward_propagation(X_valid, parameters, activation)
            cost_valid = self.cost_function(AL_valid, y_valid)

            if i%(epochs/10) == 0:
                history["epoch"].append(i)
                history["accuracy"].append(self.accuracy(X_train, y_train, parameters, activation))
                history["loss"].append(cost)
                history["val_accuracy"].append(self.accuracy(X_valid, y_valid, parameters, activation))
                history["val_loss"].append(cost_valid)
                print("Iter: {}\t Cost: {}\t Valid_Cost: {}\t Train_acc: {}\t Test_acc: {}".format(i, cost, cost_valid, self.accuracy(X_train, y_train, parameters, activation), self.accuracy(X_valid, y_valid, parameters, activation)))

        self.draw_graphs(history)
        self.save_parameters(parameters)
    

    def accuracy(self, X, Y, parameters, activation):
        
        m = Y.shape[1]
        preds, _ = self.forward_propagation(X, parameters, activation)

        Y = np.argmax(Y, 0)
        preds = np.argmax(preds, axis = 0)

        return np.round(np.sum(Y == preds)/m, 2)


    def draw_graphs(self, history):

        plt.figure(figsize=(8,5))
        plt.plot(history['loss'], label='Training Loss')
        plt.plot(history['val_loss'], label='Validation Loss')
        plt.title('Training vs Validation Loss (MLP)')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.show()

        plt.figure(figsize=(8,5))
        plt.plot(history['accuracy'], label='Training Accuracy')
        plt.plot(history['val_accuracy'], label='Validation Accuracy')
        plt.title('Training vs Validation Accuracy (MLP)')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.show()

    
    def save_parameters(self, parameters):
        np.save("model_weights.npy", parameters)


    def load_parameters(self):
        return np.load("model_weights.npy", allow_pickle=True).item()


if __name__ == "__main__":
    
    mlp = MLP()
    
    # mlp.tester_backword_propagation()

    X_train, y_train, X_valid, y_valid = mlp.get_dataset()

    parser = argparse.ArgumentParser(description="Write the model arguments")
    parser.add_argument("--layer", type=int, nargs="*", default=[31, 16, 8, 2])
    parser.add_argument("--epochs", type=int, default=1000)
    parser.add_argument("--learning_rate", type=float, default=0.0075)
    parser.add_argument("--activation_function", type=str, default="relu")

    args = parser.parse_args()

    try:
        mlp.model(X_train, y_train, X_valid, y_valid, args.layer, args.learning_rate, args.activation_function, args.epochs)
    except Exception as e:
        print(f"An error ocurred: {e}")
