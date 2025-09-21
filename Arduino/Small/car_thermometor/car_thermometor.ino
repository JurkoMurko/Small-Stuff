#include "DHT.h"
#define dataPin 10
DHT dht(dataPin, DHT11);

void setup() {
  Serial.begin(9600);
  pinMode(dataPin, INPUT_PULLUP);
  dht.begin();
  Serial.println("start");
}

void loop() {
//   float temp = dht.readTemperature(true);
   Serial.println(dht.readTemperature(true));
   delay(2000);
}
