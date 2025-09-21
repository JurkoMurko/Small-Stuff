#define pin 2

char bite;
int num;
String broh = "";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pin, OUTPUT);
  Serial.println("start");
}

void loop() {
  if (Serial.available() > 0) {
    bite = Serial.read();
    
    if ((bite >= '0') && (bite <= '9')) {
      broh += bite;
    }
    else if (bite  == '\n') {
      num = broh.toInt();
      onOff(num);
      
      // Reset var
      broh = "";
    }
    else {
      Serial.print(bite);
      Serial.println(" is an invalid charecter");
    } 
  }
}

void onOff (int timee) {
  digitalWrite(pin, HIGH);
  delay(timee);
  digitalWrite(pin, LOW);
}
