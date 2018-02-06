//AnalogTemperature Sensor

const int tempAnalogPin=A1;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int rawTemp = analogRead(tempAnalogPin);
  
  float temperatureC = (-19.0/182)*rawTemp +(1997.0/26);
  
  Serial.print("Degrees in C: ");
  Serial.println(temperatureC);
  delay(5000);
}
