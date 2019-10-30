import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rand
import Preseptron as p

rand.seed(13)


#TODO : Loading Data from irisD.csv
def ReadData():
    dataset = pd.read_csv("irisD.csv")

    print(dataset)

    return

#ReadData()
def prep(dataset):

    #dataset = pd.read_csv("iriskholoud.data",
               #      header=None)
    #dataset.to_csv("iriskholoud.data", header=None, index=False)
    ##dataset = pd.read_csv()
   # rand.shuffle(dataset)

    Train_X = dataset.iloc[:, 0:2].values
    Train_Y = dataset.iloc[:, 4].values
    # Change All Name Of Setosa
    Train_Y = np.where(Train_Y == 'Iris-setosa', -1, 1)


    len1 = np.random.permutation(len(dataset))
    X_rand=[]
    Y_rand=[]

    for i in len1:
        X_rand.append(Train_X[i])
    for i in len1:
        Y_rand.append(Train_Y[i])

    print(X_rand)
    print(Y_rand)

    return np.array(X_rand), np.array(Y_rand)

'''    if (X1 == "sepal.length"):
        x1=0
    elif(X1== "sepal.width"):
        x1=1
    elif (X1 == "petal.length"):
        x1 = 2
    elif (X1 == "petal.width"):
        x1 = 3
    if (X2 == "sepal.length"):
        x2=0
    elif(X2== "sepal.width"):
        x2=1
    elif (X2 == "petal.length"):
        x2 = 2
    elif (X1 == "petal.width"):
        x2 = 3'''


def plot_data(cls1, cls2):

    X_cls1 = []
    X_cls2 = []
    for x, y in zip(cls1, cls2):
        if y == -1:
            X_cls1.append(x)
        else:
            X_cls2.append(x)

    # convert to numpy array
    X_cls1 = np.array(X_cls1)
    X_cls2 = np.array(X_cls2)

    plt.scatter(X_cls1[:, 0], X_cls1[:, 1], color='red', marker='o', label=cls1)
    plt.scatter(X_cls2[:, 0], X_cls2[:, 1], color='blue', marker='o', label=cls2)
    plt.show()


    return




# Main
def Asmain(rate,epocs):
    dataset = pd.read_csv("iriskholoud.data", header=None)
    dataset.to_csv("iriskholoud.data", header=None, index=False)

    Xfor, Yfor = prep(dataset)

    plot_data(Xfor, Yfor)

    train_samples = 90
    # training data
    X_train, Y_train = Xfor[:train_samples], Yfor[:train_samples]

    # data for testing the efficiency
    X, Y = Xfor[train_samples:], Yfor[train_samples:]
    perseprton = p.Perceptron(X.shape[1])
    print(type(int(epocs)))

    perseprton.Think(X_train, Y_train, float(rate), int(epocs))

    perseprton.plot_decision(X, Y, X_train, Y_train)

