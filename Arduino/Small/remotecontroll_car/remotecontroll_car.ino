#define left1 2
#define left2 3
#define right1 5
#define right2 4

void left_forward() {
  digitalWrite(left1, HIGH);
  digitalWrite(left2, LOW);
}
void right_forward() {
  digitalWrite(right1, HIGH);
  digitalWrite(right2, LOW);
}
void left_backward() {
  digitalWrite(left2, HIGH);
  digitalWrite(left1, LOW);
}
void right_backward() {
  digitalWrite(right2, HIGH);
  digitalWrite(right1, LOW);
}

void forward() {
  left_forward();
  right_forward();
}

void backward() {
  left_backward();
  right_backward();
}

void clockwise_spin() {
  left_forward();
  right_backward();
}

void counterclockwise_spin() {
  right_forward();
  left_backward();
}

void off() {
  digitalWrite(left1, LOW);
  digitalWrite(left2, LOW);
  digitalWrite(right2, LOW);
  digitalWrite(right1, LOW);
}

void doo(void (*function)(), int gap) {
  (*function)();
  delay(gap);
  off();
}

void setup() {
  // put your setup code here, to run once:
  pinMode(left1, OUTPUT);
  pinMode(left2, OUTPUT);
  pinMode(right1, OUTPUT);
  pinMode(right2, OUTPUT);

  off(); 

}

void loop() {
  // put your main code here, to run repeatedly:
  delay(500);
  doo(&forward, 1100);
}
