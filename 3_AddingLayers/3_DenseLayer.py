import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

# Dense Layer
class Layer_Dense:

    # Layer Initialization
    def __init__(self, n_input, n_neurons):
        # Initialize weights and biases
        self.weights = 0.01*np.random.randn(n_input, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    # Forward pass
    def forward(self, inputs):
        # Calculate output values from inputs, weight and biases
        self.output = np.dot(inputs, self.weights) + self.biases

# Create dataset
X, y = spiral_data(samples=100, classes=3)

# Create Dense Layer with 2 input features and 3 output values
dense1 = Layer_Dense(2, 3)

dense1.forward(X)

# Lets see output of the first few samples
print(dense1.output[:5])
