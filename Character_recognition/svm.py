from sklearn import svm
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split

df = pd.read_csv('traindata.csv',header=0)

# trainData = df[300:]
# testData = df[:300]
featureColumns = ['Thumb Near', 'Thumb Far', 'Thumb/Index', 'Index Near', 'Index Far', 'Index/Middle', 'Middle Near', 'Middle Far', 'Middle/Ring', 'Ring Near', 'Ring Far', 'Ring/Little', 'Little Near', 'Little Far']
x = df[featureColumns]
# trainData = df[]
y = df['Digit']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=10)
svm_classifier = svm.SVC(kernel='linear')
svm_classifier.fit(x_train,y_train)

# testData = testData[featureColumns]

predictions = svm_classifier.predict(x_test)
# Y_known = df[:300]
# y_known = Y_known['Digit']
print accuracy_score(y_test,predictions)

# 87.69 with linear kernal