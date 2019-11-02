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
def prep(dataset,feature1,feature2,cls1,cls2):

    #dataset = pd.read_csv("iriskholoud.data",
               #      header=None)
    #dataset.to_csv("iriskholoud.data", header=None, index=False)
    ##dataset = pd.read_csv()
   # rand.shuffle(dataset)
    #Train_X= dataset.iloc[:,[feature1, feature2]].values
    #print(Train_X)
    #del dataset[:, [0, 49]].values

    print(dataset.shape)

    #a_del = np.delete(dataset, 5, 0)
    # a_del= np.delete(dataset, np.s_[0:5], axis=0)

    # print(a_del.shape)

    #######################################################################
    Train_X1 =dataset.iloc[:,[feature1, feature2]].values
    Train_Y1 = dataset.iloc[:, 4].values

    #for delete spefic Data

    if(cls1!= "Iris-setosa" and cls2!="Iris-setosa"):
        Train_X = np.delete(Train_X1, np.s_[0:50], axis=0)
        Train_Y = np.delete(Train_Y1, np.s_[0:50])
        print(Train_X)
    elif(cls1!="Iris-versicolor"and cls2!="Iris-versicolor"):
        Train_X = np.delete(Train_X1, np.s_[50:100], axis=0)
        Train_Y = np.delete(Train_Y1, np.s_[50:100])
        print(Train_X)

    else:

        Train_X = np.delete(Train_X1, np.s_[100:150], axis=0)
        Train_Y = np.delete(Train_Y1, np.s_[100:150])
        print("version",Train_X)





    print(len(Train_X))
    #if(Train_Y=="Iris-setosa")
    Train_Y = np.where(Train_Y == cls1, -1,1)
    #Train_Y = np.replace(Train_Y == cls1, -1)




    print(Train_Y)



    len1 = np.random.permutation(len(Train_X))
    X_rand = []
    Y_rand = []
    for i in len1:
        X_rand.append(Train_X[i])

    for i in len1:
        Y_rand.append(Train_Y[i])

    return np.array(X_rand), np.array(Y_rand)




def plot_data(cls1, cls2):

    X_cls1 = []
    X_cls2 = []
    print("kk",len(cls1))
    for x, y in zip(cls1, cls2):
        if y == -1:
            X_cls1.append(x)
        else:
            X_cls2.append(x)

    X_cls1 = np.array(X_cls1)
    X_cls2 = np.array(X_cls2)
    plt.scatter(X_cls1[:, 0], X_cls1[:, 1], color='red', marker='o', label=cls1)
    plt.scatter(X_cls2[:, 0], X_cls2[:, 1], color='blue', marker='o', label=cls2)
    plt.show()


    return




# Main
def Asmain(rate,epocs,feature1,feature2,cls1,cls2):
    dataset = pd.read_csv("iriskholoud.data", header=None)
    dataset.to_csv("iriskholoud.data", header=None, index=False)
    if(feature1=='sepal.length'):
        feature1=0
    elif(feature1=='sepal.width'):
        feature1=1
    elif (feature1 == 'petal.length'):
        feature1 = 2
    elif (feature1 == 'petal.width'):
        feature1=3

    if (feature2== 'sepal.length'):
        feature2 = 0
    elif (feature2 == 'sepal.width'):
        feature2 = 1
    elif (feature2 == 'petal.length'):
        feature2 = 2
    elif (feature2== 'petal.width'):
        feature2 = 3
    print("ff",cls1)
    Xfor,Yfor= prep(dataset,feature1,feature2,cls1,cls2)
    print(Yfor)
    plot_data(Xfor, Yfor)

    train_samples = 60
    print(len(Yfor))
    X_train, Y_train = Xfor[:train_samples], Yfor[:train_samples]

    X, Y = Xfor[train_samples:], Yfor[train_samples:]
    perseprton = p.Perceptron(X.shape[1])
    perseprton.Think(X_train, Y_train, 0.2, 12)
    perseprton.plot_decision(X, Y, X_train, Y_train)


