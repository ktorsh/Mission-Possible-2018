//AnalogTemperature Sensor

const int tempAnalogPin=A1;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int rawReading = analogRead(tempAnalogPin);
  float voltage = rawReading*5.0/1024.0;
  float temperatureC = (voltage-0.5)*100;
  Serial.print("Degrees in C: ");
  Serial.println(termperatureC);
}
