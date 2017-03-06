import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import normalize
#Serializing and storing the classifier for server purposes
import pickle

df = pd.read_csv("D:/Vacation/ML/sangam/created_dataset_play_7.csv", header=None)
#Getting dimensions
train_n, train_m = df.shape
#Creating numpy array
X_train = np.zeros(shape=(train_n, 9))
y_train = np.zeros(shape=(train_n, 1))
#Getting the values
X_train[:, :] = df.iloc[0:train_n, [0, 1, 2, 3, 4, 5, 6, 7, 8]].values
y_train[:, :] = df.iloc[0:train_n, [9]].values
#Normalizing the Data
X_train = normalize(X_train)
#Training Data
mlp = MLPClassifier(hidden_layer_sizes=(100, 200, 100))
mlp.fit(X_train, y_train)
#Saving the classifier
filename = 'D:/Vacation/ML/sangam/main/classifier.sav'
pickle.dump(mlp, open(filename, 'wb')) 