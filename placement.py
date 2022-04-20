# -*- coding: utf-8 -*-
import pandas as pd#to read the csv file
import numpy as np #NumPy is used for working with arrays.
import pickle

dataframe=pd.read_csv('collegePlace.csv')
dataframe.head()
dataframe.shape
dataframe['Gender'].replace({'Male':'1','Female':'0'},inplace=True)
dataframe.head()
dataframe['Stream'].unique()
dataframe['Stream'].replace({'Electronics And Communication':'0','Computer Science':'1','Information Technology':'2','Mechanical':'3','Electrical':'4','Civil':'5'},inplace=True)
dataframe.head()
dataframe.isnull().sum() # checking null values

Y=dataframe['PlacedOrNot']
X=dataframe.drop(['PlacedOrNot'],axis=1)

"""### train_test_split"""

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

"""## Decision Tree """

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
dtree.fit(X_train, Y_train)


#Saving model to disk
pickle.dump(dtree, open('placement.pkl','wb'))

#Loading model 
placement = pickle.load(open('placement.pkl','rb'))

