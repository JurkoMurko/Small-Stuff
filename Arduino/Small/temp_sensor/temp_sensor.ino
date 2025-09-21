#include "DHT.h"

#define dataPin 10
#define heatPin 3
#define coolPin 4
#define buttonDOWN 6
#define buttonUP 5

#define type DHT22

DHT dht(dataPin, type);

bool heat;
bool cool;
  
int upState = 1;
int pastUpState = 1;
int downState = 1;
int pastDownState = 1;

float target = 75.0;
const float error = 0.7;
const int clockLength = 100;  // must be a factor of 2000

void setup() {
    Serial.begin(9600);
    pinMode(dataPin, INPUT_PULLUP);
    pinMode(heatPin, OUTPUT);

    pinMode(buttonUP, INPUT_PULLUP);
    pinMode(buttonDOWN, INPUT_PULLUP);

    dht.begin();

    Serial.println("start");
}

void modeUpdate(float curTemp) {
  // logic
  // I could have used subraction instead of all this convoluted bullshit
  if (target - error < curTemp && curTemp < target + error) {
    heat = false;
    cool = false;
  } else if (curTemp > target) {
    cool = true;
    heat = false;

  } else if (curTemp < target) {
    cool = false;
    heat = true;
  }
}

void relayUpdate() {
  // controller or switch
  if (heat) {
    digitalWrite(heatPin, HIGH);
  } else {
    digitalWrite(heatPin, LOW);
  }
  if (cool) {
    digitalWrite(coolPin, HIGH);
  } else {
    digitalWrite(coolPin, LOW);
  }
}

void targetUpdate(int upState, int pastUpState, int downState, int pastDownState) {
  // target update
  if (upState == 0 && pastUpState == 1) {
    target++;
  }
  if (downState == 0 && pastDownState == 1) {
    target--;
  }
}

void loop() {
  float temp = dht.readTemperature(true);
    
  for (int i = 0; i < 2000 / clockLength; i++) {    
    int upState = digitalRead(buttonUP);
    int downState = digitalRead(buttonDOWN);
  
    targetUpdate(upState, pastUpState, downState, pastDownState);
    modeUpdate(temp);
    relayUpdate();
    
    Serial.println(temp);

    // update last state
    pastUpState = upState;
    pastDownState = downState;

    delay(clockLength);
  }
  delay(50);
}
