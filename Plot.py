import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#TODO : Build Plots
def Plots(X1,X2):
    iris = pd.read_csv("irisD.csv")
    for n in range(0, 150):
        if iris['variety'][n] == 'Setosa':
            plt.scatter(iris[X1][n], iris[X2][n], color='red')
            plt.xlabel(X1)
            plt.ylabel(X2)
        elif iris['variety'][n] == 'Versicolor':
            plt.scatter(iris[X1][n], iris[X2][n], color='blue')
            plt.xlabel(X1)
            plt.ylabel(X2)
        elif iris['variety'][n] == 'Virginica':
            plt.scatter(iris[X1][n], iris[X2][n], color='green')
            plt.xlabel(X1)
            plt.ylabel(X2)
    plt.show()


'''

def Plots(X1,X2):
    iris = pd.read_csv("irisD.csv")
    if (X1 == "X1" and X2 == "X2"):
        for n in range(0,150):
            if iris['variety'][n] == 'Setosa':
                plt.scatter(iris['sepal.length'][n], iris['sepal.width'][n], color='red')
                plt.xlabel('sepal.length')
                plt.ylabel('sepal.width')
            elif iris['variety'][n] == 'Versicolor':
                plt.scatter(iris['sepal.length'][n], iris['sepal.width'][n], color='blue')
                plt.xlabel('sepal.length')
                plt.ylabel('sepal.width')
            elif  iris['variety'][n] == 'Virginica':
                plt.scatter(iris['sepal.length'][n], iris['sepal.width'][n], color='green')
                plt.xlabel('sepal.length')
                plt.ylabel('sepal.width')
        plt.show()
    elif(X1 == "X1" and X2 == "X1"):
        for n in range(0,150):
            if iris['variety'][n] == 'Setosa':
                plt.scatter(iris['sepal.length'][n], iris['sepal.length'][n], color='red')
                plt.xlabel('sepal.length')
                plt.ylabel('sepal.length')
            elif iris['variety'][n] == 'Versicolor':
                plt.scatter(iris['sepal.length'][n], iris['sepal.length'][n], color='blue')
                plt.xlabel('sepal.length')
                plt.ylabel('sepal.length')
            elif  iris['variety'][n] == 'Virginica':
                plt.scatter(iris['sepal.length'][n], iris['sepal.length'][n], color='green')
                plt.xlabel('sepal.length')
                plt.ylabel('sepal.length')
        plt.show()
    elif (X1 == "X1" and X2 == "X3"):
        for n in range(0, 150):
            if iris['variety'][n] == 'Setosa':
                plt.scatter(iris['sepal.length'][n], iris['petal.length'][n], color='red')
                plt.xlabel('sepal.length')
                plt.ylabel('petal.length')
            elif iris['variety'][n] == 'Versicolor':
                plt.scatter(iris['sepal.length'][n], iris['petal.length'][n], color='blue')
                plt.xlabel('sepal.length')
                plt.ylabel('petal.length')
            elif iris['variety'][n] == 'Virginica':
                plt.scatter(iris['sepal.length'][n], iris['petal.length'][n], color='green')
                plt.xlabel('sepal.length')
                plt.ylabel('petal.length')
        plt.show()
    elif (X1 == "X1" and X2 == "X4"):
        for n in range(0, 150):
            if iris['variety'][n] == 'Setosa':
                plt.scatter(iris['sepal.length'][n], iris['petal.width'][n], color='red')
                plt.xlabel('sepal.length')
                plt.ylabel('petal.width')
            elif iris['variety'][n] == 'Versicolor':
                plt.scatter(iris['sepal.length'][n], iris['petal.width'][n], color='blue')
                plt.xlabel('sepal.length')
                plt.ylabel('petal.width')
            elif iris['variety'][n] == 'Virginica':
                plt.scatter(iris['sepal.length'][n], iris['petal.width'][n], color='green')
                plt.xlabel('sepal.length')
                plt.ylabel('petal.width')
        plt.show()





'''
