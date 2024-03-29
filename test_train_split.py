# -*- coding: utf-8 -*-
"""test_train_split.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lBvBkLln7LQUln4GRRQG0iNAkgYYkfzR
"""

import os
os.getcwd()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df= pd.read_csv("/content/sample_data/Iris.csv")
df.head()

df["Species"].value_counts ()

df.isnull().sum()

df.describe()

df['SepalLengthCm'].hist()
df['SepalWidthCm'].hist()

df['PetalLengthCm'].hist()
df['PetalWidthCm'].hist()

sns.pairplot (df, hue= "Species")

from sklearn.model_selection import train_test_split

x= df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
y= df["Species"]
x_train, x_test, y_train, y_test= train_test_split (x,y, test_size=0.3)

from sklearn.ensemble import RandomForestClassifier
clf= RandomForestClassifier(n_estimators= 100)
clf.fit(x_train, y_train)
y_pred= clf.predict (x_test)

from sklearn import metrics
print ("Accuracy:", metrics.accuracy_score (y_test, y_pred))

from sklearn.preprocessing import LabelEncoder
le= LabelEncoder ()

df['Species']= le.fit_transform (df['Species'])
df.head()

X= df.drop (columns= ['Species'])
Y= df['Species']
x_train, x_test, y_train, y_test= train_test_split (X,Y, test_size= 0.4)

from sklearn.linear_model import LinearRegression
lr= LinearRegression()

lr.fit(x_train, y_train)

print ('Accuracy:', lr.score(x_test, y_test))

"""#Accurancy Scores of Iris Dataset
1. RandomForestClassifier is 93.3%
2. Linearregression is 96.80%
"""