import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random as rand

class Perceptron:

    def __init__(self, num):
        # it for Add bais  As 1
        #
        self.wight = np.zeros(1 + num)


        return



    def activationSum(self, X):

        return np.dot(X, self.wight[1:]) + self.wight[0]



    def partition(self, X):

        return np.where(self.activationSum(X) >= 0.0, 1, -1)

    def Think(self, X_train, Y_train, eta=0.01, epochs=10):

        self.train_errors= []

        for _ in range(epochs):
            err = 0
            for x, y in zip(X_train, Y_train):
                update = eta * (y - self.partition(x))
                self.wight[1:] += update * x
                self.wight[0] += update
                err += int(update != 0.0)
            self.train_errors.append(err)

        return

    def plot_decision(self, X, Y, X_train, Y_train):

        x1_min, x1_max = X[:, 0].min() - 2, X[:, 0].max() + 2
        x2_min, x2_max = X[:, 1].min() - 2, X[:, 1].max() + 2

        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, .02),
                               np.arange(x2_min, x2_max, .02))

        # start new plot
        fig = plt.figure()
        axs = plt.gca()

        x_mesh = np.array([xx1.ravel(), xx2.ravel()]).T
        Z = self.partition(x_mesh)
        Z = Z.reshape(xx1.shape)

        axs.contourf(xx1, xx2, Z, alpha=0.4, cmap=matplotlib.colors.ListedColormap(['red', 'blue']))
        axs.set_xlim(xx1.min(), xx1.max())
        axs.set_ylim(xx2.min(), xx2.max())

        X_setosa = []
        X_other = []
        for x, y in zip(X, Y):
            if y == -1:
                X_setosa.append(x)
            else:
                X_other.append(x)

        X_setosa = np.array(X_setosa)
        X_other = np.array(X_other)

        axs.scatter(X_setosa[:, 0], X_setosa[:, 1],
                    color='red', marker='.', label='Setosa')
        axs.scatter(X_other[:, 0], X_other[:, 1],
                    color='blue', marker='.', label='Other')

        X_setosa = []
        X_other = []
        for x, y in zip(X_train, Y_train):
            if y == -1:
                X_setosa.append(x)
            else:
                X_other.append(x)

        X_setosa = np.array(X_setosa)
        X_other = np.array(X_other)

        axs.scatter(X_setosa[:, 0], X_setosa[:, 1],
                    color='red', marker='x')
        axs.scatter(X_other[:, 0], X_other[:, 1],
                    color='blue', marker='x')


        axs.set_title('Perceptron')
        plt.show()


        return






