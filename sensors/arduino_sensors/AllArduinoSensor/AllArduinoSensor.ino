//Prints all sensor data to the Serial Moniter

const int hallAnalogPin=A0;
const int tempAnalogPin=A1;
const int photoAnalogPin=A2;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int rawHall = analogRead(hallAnalogPin);
  
  int rawTemp = analogRead(tempAnalogPin);
  float voltageTemp = rawTemp*5.0/1024.0;
  float temperatureC = (voltageTemp-0.5)*100;

  int rawPhoto = analogRead(photoAnalogPin);

  Serial.print(rawHall);
  Serial.print(",");
  Serial.print(temperatureC);
  Serial.print(",");
  Serial.print(rawPhoto);  
}
