import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import normalize
#Serializing and storing the classifier for server purposes
import pickle

#print("------------------------------------------------------------------------")
#print("YO!")
#print("------------------------------------------------------------------------")
#print("Using my brains YO....")
#print("------------------------------------------------------------------------")

df = pd.read_csv("D:/Vacation/ML/sangam/created_dataset_play_7.csv", header=None)
#df_test = pd.read_csv("D:/Vacation/ML/sangam/test_run_1.csv", header=None)
#Getting dimensions
train_n, train_m = df.shape
#test_n, test_m = df_test.shape
#Creating numpy array
X_train = np.zeros(shape=(train_n, 9))
#X_test = np.zeros(shape=(test_n, 9))
#X_test_2 = np.zeros(shape=(test_n, 9))
y_train = np.zeros(shape=(train_n, 1))
#y_test = np.zeros(shape=(test_n, 1))
#y_test_2 = np.zeros(shape=(test_n, 1))
#Getting the values
X_train[:, :] = df.iloc[0:train_n, [0, 1, 2, 3, 4, 5, 6, 7, 8]].values
#X_test[:, :] = df.iloc[0:test_n, [0, 1, 2, 3, 4, 5, 6, 7, 8]].values
y_train[:, :] = df.iloc[0:train_n, [9]].values
#y_test[:, :] = df.iloc[0:test_n, [9]].values

#X_test_2[:, :] = df_test.iloc[0:test_n, [0, 1, 2, 3, 4, 5, 6, 7, 8]].values
#y_test_2[:, :] = df_test.iloc[0:test_n, [9]].values
#Normalizing the Data
X_train = normalize(X_train)
#X_test = normalize(X_test)
#Training Data
print("Training data....")
print("------------------------------------------------------------------------")
mlp = MLPClassifier(hidden_layer_sizes=(100, 200, 100))
mlp.fit(X_train, y_train)
print("Training successful!")
print("------------------------------------------------------------------------")
#Testing the data accuracy
#X_test_2 = normalize(X_test_2)
#predicted = mlp.predict(X_test_2)
#print(accuracy_score(y_test_2, predicted))
#Saving the classifier
filename = 'D:/Vacation/ML/sangam/classifier_7.sav'
pickle.dump(mlp, open(filename, 'wb')) 
'''
#Deploying the server
print("Deploying the classifier....")
print("------------------------------------------------------------------------")
classifier = pickle.load(open(filename, 'rb'))
X_test = normalize(X_test)
print("Working on accuracy....")
print("------------------------------------------------------------------------")
predicted = classifier.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, predicted)*100, "%")
#print("F**K YOU HUMANS!@!")
print("------------------------------------------------------------------------")
'''