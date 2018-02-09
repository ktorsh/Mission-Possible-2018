//Prints all sensor data to the Serial Moniter

const int hallAnalogPin=A0;
const int tempAnalogPin=A1;
//const int photoAnalogPin=A2;
const int gasAnalogPin=A2;

const int lbump=7;
const int rbump=3;

void setup() {
  Serial.begin(9600);
  pinMode(lbump, INPUT);
  digitalWrite(lbump, HIGH);
  pinMode(rbump, INPUT);
  digitalWrite(rbump, HIGH);
}

void loop() {
  int rawHall = analogRead(hallAnalogPin);
  
  int rawTemp = analogRead(tempAnalogPin);
  float temperatureC = (-19.0/182)*rawTemp +(1997.0/26);

  int rawGas = analogRead(gasAnalogPin);

  int ltouch=digitalRead(lbump);
  int rtouch=digitalRead(rbump);

  String comma=",";
  String printStatement=rawHall+comma+temperatureC+comma+rawGas+comma+ltouch+comma+rtouch;

  Serial.println(printStatement);
  delay(1000);
}
