import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Perceptron :
    def __init__(self, activation="sigmoid", learning_rate=.01, epoch=1000, gradient= False):
        self.activation = activation
        self.learning_rate = learning_rate
        self.epoch = epoch
        self.gradient = gradient
        self.weights = None
        self.bais = 0

    def _unit_step(self,z):
        return np.where(z>=0, 1, 0)
    
    def _relu(self, z):
        return np.maximum(0, z)
    
    def _sigmoid(self, z):
        return 1 / (1+np.exp(-z))
    
    def _gradient_descent(self, X, y):
        if self.activation == "sigmoid":
            for _ in range(self.epoch):
                y_hat = self.predict(X)
                error = y - y_hat
                self.weights += self.learning_rate * self.n_samples/2 * X.T.dot(error*y_hat*(1-y_hat))
                self.bais += self.learning_rate * self.n_samples/2 * np.sum(error*y_hat*(1-y_hat))
        elif self.activation == "relu":
            for _ in range(self.epoch):
                y_hat = self.predict(X)
                error = y-y_hat
                self.weights += self.learning_rate * self.n_samples/2 * X.T.dot(error*(y_hat>0))
                self.bais += self.learning_rate * self.n_samples/2 * np.sum(error*(y_hat>0))
        else:
            raise ValueError("only sigmoid and relu can use gradient descnet")

    def _perceptron_update_rule(self, X ,y):
        for _ in range(self.epoch):
            y_hat = self.predict(X)
            error = y-y_hat
            self.weights += self.learning_rate * X.T.dot(error)
            self.bais += self.learning_rate * np.sum(error)
    
    def fit(self, X, y):
        y = y.reshape(-1, 1)
        self.n_samples, n_features = X.shape
        self.weights = np.zeros((n_features, 1))
        if self.gradient :
            self._gradient_descent(X, y)
        else:
            self._perceptron_update_rule(X, y)


    def predict(self, X):
        z = X.dot(self.weights) + self.bais
        if self.activation == "unit_step":
            y_hat = self._unit_step(z)
        elif self.activation == "relu":
            y_hat = self._relu(z)
        elif self.activation == "sigmoid":
            y_hat = self._sigmoid(z)
        else:
            raise ValueError("only sigmoid, relu, unit step are supported")
        return y_hat
    
    