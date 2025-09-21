#include <Servo.h> 

Servo serX;
Servo serY;

String in;
float float_in;
int x, y;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
  
  serX.attach(2);
  serY.attach(3);
}

void loop() {
  if (Serial.available() > 0) {
//    Serial.println("Serial is available");
    in = Serial.readString();
//    Serial.println("Input= " + in);
    float_in = in.toFloat();
    
    x = float_in / 1000; // first 3 nums of a six digit num
    y = float_in - x * 1000;  // last three nums

    Serial.print("X: ");
    Serial.print(x);
    Serial.print("  Y: ");
    Serial.print(y);
  }
    
  serX.write(x);
  serY.write(y);
}
