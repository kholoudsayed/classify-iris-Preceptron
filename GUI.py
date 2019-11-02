import  tkinter
import Plot as pol
from  tkinter import *
from matplotlib import pyplot as plt
import tot as t
from PIL import ImageTk,Image
from  tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton

import numpy as np


#TODO : make Window there Size 800*200
window  =Tk()
# that is for window
window.title("Computational Intelligence Tasks")
window.geometry("1800x1000")


##########################################################
#TODO : make Array for Fields Entry

ValueFeature = ["sepal.length","sepal.width","petal.length","petal.width"]
ValueClass=["Iris-setosa","Iris-versicolor","Iris-virginica"]
####################################################
#TODO : make lable for Description the Task

#lable
title= Label(text="Task 1 :  Apply Single Layer Perceptron on Iris Data  ",bg="pink")
title.grid(column=0,row=0)

#######################################################################
# feature 1
#TODO : make comboBox for Entry Feature number One

titlefeature1 = Label( text="Choose your frist Feature 1:")
titlefeature1.grid(column=0,row=1)


combo=Combobox(window,values=ValueFeature,state='readonly')
combo.current(0)

combo.grid(column=1, row=1)
#########################################################################
#TODO : make comboBox for Entry Feature number Two

# feature 2
titlefeature2 = Label( text="Choose your Second Feature 2:")
titlefeature2.grid(column=2,row=1)


combo2=Combobox(window,values=ValueFeature,state='readonly')
combo2.current(0)

combo2.grid(column=3, row=1)


####################################
#buttton for Plots
#TODO : Button for Plots

buttonplots =Button(text="Plots..." ,bg="pink",command= lambda: pol.Plots(combo.get(),combo2.get()))

buttonplots.grid(column=4,row=1)
###########################################################################
# Class 1
#TODO : make comboBox for Entry Class number one

titleClass1= Label( text="Choose your Frist Class :")
titleClass1.grid(column=0,row=2)

comboclass1=Combobox(window,values=ValueClass,state='readonly')
comboclass1.current(0)

comboclass1.grid(column=1, row=2)




#################################################################################
#class 2
#TODO : make comboBox for Entry Class number Two

titleClass2= Label( text="Choose your Second Class :")
titleClass2.grid(column=2,row=2)


comboclass2=Combobox(window,values=ValueClass,state='readonly')
comboclass2.current(0)

comboclass2.grid(column=3, row=2)

#################################################################################
#TODO : make entry To get Learning Rate

#learning Rate
titleLearningRate= Label( text="learning Rate :",bg="pink")
titleLearningRate.grid(column=0,row=3)

entryfiledRate=Entry()

entryfiledRate.grid(column=1,row=3)
#################################################################################
#Epochs
#TODO : make entry To get Epochs

titleEpochs=Label( text="Epochs :",bg="pink")
titleEpochs.grid(column=2,row=3)


entryfiledEpochs=Entry()
entryfiledEpochs.grid(column=3,row=3)

###################################################################################
#Bais
#TODO : make entry To get Bais

var = IntVar()
Checkbox =Checkbutton(window,text="Bais",variable=var)

Checkbox.grid(column=4,row=3)
#######################################################################
#button
#TODO : Button RUN
string_answer = entryfiledEpochs.get()
print(type(string_answer))
buttonRun =Button(text="Run..." ,bg="pink",command =lambda  :t.Asmain(entryfiledRate.get(),entryfiledEpochs.get(),combo.get(),combo2.get(),comboclass1.get(),comboclass2.get()))
#buttonRun =Button(text="Run..." ,bg="cyan",command= lambda: tst.Presptron(combo.get(),combo2.get(),comboclass1.get(),comboclass2.get(),entryfiledRate.get(),entryfiledEpochs.get(),var.get()))
buttonRun.grid(column=1,row=4)


bg_image = PhotoImage(file = "sakura.png")
x = Label (image = bg_image)
x.grid(row = 4, column = 5)


#window.configure(background='pink')

window.mainloop()


