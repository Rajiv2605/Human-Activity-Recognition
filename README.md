# IOT Implementation of Human Activity Recognition
In this project, I have implemented a Python Flask based server which recieves requests from the Node MCU containing sensor values.
I have trained a ML classifier containing **multi-layered neural networks** on the data collected while the person is **walking**, **running** and **stationary**.
**Features**: Inertial signals obtained from the accelerometer and gyroscope of Node MCU.
**Classes**: Walking, Running, Stationary
The classifier predicts the class using the sensor values recieved from the Node MCU.
The server correspondingly updates the time spent in the corresponding activity.
The server then returns a JSON containing key-value pairs of the classes and their corresponding time-spent value.
