import numpy as np


# FUNCTION IMPLEMENTATION
def sigmoid(x, derivative=False):
  return x*(1-x) if derivative else 1.0/(1 + np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)


# CLASS IMPLEMENTATION (Credits: James Loy)
class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4)
        self.weights2   = np.random.rand(4,1)
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T, (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2


# APPLICATION
X = np.array([[0,0,1,1],
              [0,1,0,1],
              [1,1,1,1]]).T
Y = np.array([[0],[1],[1],[0]])
ANN = NeuralNetwork(X,Y)

print("Before Training-")
print("x1, x2, x3:")
print(ANN.input)
print("y1:")
print(ANN.y)
print("Output")
print(ANN.output)
print("\n")


# 5000 Iterations
i = 1
while i <= 5000:
    ANN.feedforward()
    ANN.backprop()
    i = i + 1
print("After Training-")
print(ANN.output)

