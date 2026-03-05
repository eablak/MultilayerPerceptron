import numpy as np
import os


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

        for i in range(0, epochs):

            AL, forward_cache = self.forward_propagation(X_train, parameters, activation)
            cost = self.cost_function(AL, y_train)
            grads = self.backward_propagation(AL, y_train, parameters, forward_cache, activation)
            parameters = self.update_parameters(parameters, grads, learning_rate)

            if i%(epochs/10) == 0:
                print("Iter: {}\t Cost: {}\t Train_acc: {}\t Test_acc: {}".format(i, cost, self.accuracy(X_train, y_train, parameters, activation), self.accuracy(X_valid, y_valid, parameters, activation)))

        return parameters
    

    def accuracy(self, X, Y, parameters, activation):
        
        m = Y.shape[1]
        preds, _ = self.forward_propagation(X, parameters, activation)

        Y = np.argmax(Y, 0)
        preds = np.argmax(preds, axis = 0)

        return np.round(np.sum(Y == preds)/m, 2)



if __name__ == "__main__":
    
    mlp = MLP()
    
    # mlp.tester_backword_propagation()

    X_train, y_train, X_valid, y_valid = mlp.get_dataset()
    layer_dims = [X_train.shape[0], 16, 8, y_train.shape[0]]
    learning_rate = 0.0075
    epochs = 1000

    parameters = mlp.model(X_train, y_train, X_valid, y_valid, layer_dims, learning_rate, "relu", epochs)