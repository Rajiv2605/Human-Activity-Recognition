#include<ESP8266HTTPClient.h>
#include<ESP8266WiFi.h>
#include<ArduinoJson.h>

void connectToWifi()
{
  Serial.begin(9600);
  WiFi.begin("Tiger Gate", "rajiv12345678");
  while(WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.println("Waiting for connection...");
  }
}

void sendDataToServer()
{
  
  if(WiFi.status()==WL_CONNECTED)
  {
    Serial.println("Hurray!!Connected!");
    // put your main code here, to run repeatedly:
    StaticJsonBuffer<300> JSONbuffer;
    JsonObject& JSONencoder = JSONbuffer.createObject();
    // creating sample JSON data
    JSONencoder["sensorType"] = "Temperature";
    // creating a json array for sending array of data
    JsonArray& values = JSONencoder.createNestedArray("values");
    values.add(20);
    values.add(30);
    values.add(40);
    // Printing the json into the character buffer
    char JSONmessageBuffer[300];
    JSONencoder.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
    Serial.println(JSONmessageBuffer);
    // Doing a HTTP request
    HTTPClient http;
    http.begin("http://192.168.43.214:5000/");
    http.addHeader("Content-Type", "application/json");
    //Getting connection response from the server
    int httpCode = http.POST(JSONmessageBuffer);
    String payload = http.getString();
    Serial.println(httpCode);
    Serial.println(payload);
    http.end();
  }
  else
  {
    Serial.println("Error in WiFi connection");   
  }
  //delay(1000);  //Send a request every second
}

void setup() {
  connectToWifi();
}

void loop() {
  sendDataToServer();
}
