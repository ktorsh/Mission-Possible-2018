//Analog Hall Switch Testing Code
const int hallAnalogPin=A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(analogRead(hallAnalogPin));
}
