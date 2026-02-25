import numpy as np


class MLP:
    
    def __init__(self, input_size, hidden_size, output_size):

        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        layers = [self.input_size] + self.hidden_size + [self.output_size]

        self.weights = []
        for i in range(len(layers)-1):
            w = np.random.randn(layers[i], layers[i+1])
            self.weights.append(w)
        

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    

    def softmax(self, x):
        
        exponent = np.exp(x)
        return exponent/exponent.sum(axis=1,keepdims=True)
        

    def forward_propagate(self, inputs):
        activations = inputs

        # Compute hidden and output layer inputs and outputs: Apply activation functions to compute the activations
        for w in self.weights:
            net_inputs = np.dot(activations, w)
            activations = self.sigmoid(net_inputs)
        
        output = self.softmax(activations[-1])
        return output


    def backward_propagate(self, X, y, output, learning_rate):
        # Compute errors and update weights and biases: Adjust the weights and biases using the gradient descent algorithm

        output_error = output - y
        hidden_error = np.dot(output_error, self.weights_hidden_output.T) * self.hidden_output * (1 - self.hidden_output)

        self.weights_hidden_output -= learning_rate * np.dot(self.hidden_output.T, output_error)
        self.bias_output -= learning_rate * np.sum(output_error, axis=0, keepdims=True)
        self.weights_input_hidden -= learning_rate * np.dot(X.T, hidden_error)
        self.bias_hidden -= learning_rate * np.sum(hidden_error, axis=0, keepdims=True)

    
    def train(self, X, y, epochs, learning_rate):
        # Train the network: Perform forward and backward propagation for a specified number of epochs and print the loss periodically

        for epoch in range(epochs):
            output = self.forward_propagate(X)
            self.backward_propagate(X, y, output, learning_rate)
            if (epoch+1) % 100 == 0:
                loss = -np.sum(y * np.log(output)) / X.shape[0]
                print(f"Epoch {epoch+1}, Loss: {loss:.4f}")

    
    def predict(self, X):
        # Make predictions: Compute the output and return the predicted class labels

        output = self.forward_propagate(X)
        return np.argmax(output, axis=1)