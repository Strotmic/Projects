licht = A0;
pot = A1;
float potValue;
float potVolt;
float lichtValue;
float lichtPercentage;

void setup() {
  Serial.begin(9600);
  pinMode(licht, INPUT);
  pinMode(pot, INPUT);
}

float analogToVolt(value) {
  return (value/1023.0)*5;
}

float analogToPercent(value) {
  return (value/1023.0) * 100.0;
}

void loop() {
  // simple echo server

  potValue = analogRead(pot);
  potVolt = analogToVolt(potValue);

  lichtValue = analogRead(licht);
  lichtPercentage = analogToPercent(lichtValue);

  if (Serial.available()>0) {
    String line = Serial.readString();
    if (line == "sensor_1") {
        Serial.println("Licht Procent: ");
        Serial.println(lichtPercentage);
      }
    if (line == "sensor_2") {
      Serial.println("Pot Value: ");
      Serial.println(PotVolt);
    }
  }
}
