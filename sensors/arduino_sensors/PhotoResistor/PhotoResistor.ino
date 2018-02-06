//PhotoResistor *just in case

const int photoAnalogPin=A2;
void setup() {
  Serial.begin(9600);

}

void loop() {
  Serial.println(analogRead(photoAnalogPin));
}
