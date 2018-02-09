//Bump Sensor

const int lbump=7;
const int rbump=3;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(lbump, INPUT);
  digitalWrite(lbump, HIGH);
  pinMode(rbump, INPUT);
  digitalWrite(rbump, HIGH);
}

void loop() {
  if (digitalRead(lbump)==1){
    Serial.println("HI");
  }
  delay(1000);
}
