//Prints all sensor data to the Serial Moniter

const int hallAnalogPin=A0;
const int tempAnalogPin=A1;
//const int photoAnalogPin=A2;
const int gasAnalogPin=A2;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int rawHall = analogRead(hallAnalogPin);
  
  int rawTemp = analogRead(tempAnalogPin);
  float temperatureC = (-19.0/182)*rawTemp +(1997.0/26);

  int rawGas = analogRead(gasAnalogPin);

  String printStatement=rawHall+","+temperatureC+","+rawGas;

  Serial.println(printStatement);
  delay(2000);
}
