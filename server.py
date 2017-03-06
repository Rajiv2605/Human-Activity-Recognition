"""
Creating a server for activity recognition
"""
from flask import Flask, jsonify, request
import numpy as np
import pickle
from sklearn.preprocessing import normalize


app = Flask('__name__')
filename = 'D:/Vacation/ML/sangam/classifier_7.sav'
time = [0, 0, 0]
check=0
init_time=0
i=0
checkState=False
global_n=1
data = {"walking":str(time[0])+",0", "running":str(time[1])+",0", "standing":str(time[2])+",0"}

@app.route('/', methods = ['GET', 'POST'])
def index():
    global time
    global check
    global data
    global i
    global global_n
    global init_time
    global checkState
    arduino_data = request.get_json()

    if request.method=="GET":
        return jsonify(data)
    else:
        sensorValues = arduino_data["values"]
        print(sensorValues)
        X_test = np.array(sensorValues[0:9])
        classifier = pickle.load(open(filename, 'rb'))
        n = classifier.predict(normalize(X_test))

        matcher = {'1':"walking", '2':"running", '3':"standing"}
        print("")
        print("")
        print("The person appears to be " + matcher[str(int(n))] + ".")
        print("")
        print("")

        time[int(n)-1]+=0.04

        data = {"walking":str(time[0])+",0", "running":str(time[1])+",0", "standing":str(time[2])+",0"}

        return jsonify(data)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')