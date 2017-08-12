from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split

df = pd.read_csv('traindata.csv',header=0)


featureColumns = ['Thumb Near', 'Thumb Far', 'Thumb/Index', 'Index Near', 'Index Far', 'Index/Middle', 'Middle Near', 'Middle Far', 'Middle/Ring', 'Ring Near', 'Ring Far', 'Ring/Little', 'Little Near', 'Little Far']
x = df[featureColumns]
y = df['Character']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=10)
ann_classifier = MLPClassifier()
ann_classifier.fit(x_train,y_train)


predictions = ann_classifier.predict(x_test)

print accuracy_score(y_test,predictions)

# 99.18388