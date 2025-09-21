#define toggle_left 3
#define toggle_right 4
#define direction_left 5  // these are hardwired to forward
#define direction_right 6  // these are hardwired to forward

void left_forward() {
  digitalWrite(direction_left, LOW);
  digitalWrite(toggle_left, HIGH);
}

void right_forward() {
  digitalWrite(direction_right, LOW);
  digitalWrite(toggle_right, HIGH);}

void left_backward() {
  digitalWrite(direction_left, HIGH);
  digitalWrite(toggle_left, HIGH);
}

void right_backward() {
  digitalWrite(direction_right, HIGH);
  digitalWrite(toggle_right, HIGH);
}

void left_off() {
  digitalWrite(toggle_left, LOW);
}

void right_off() {
  digitalWrite(toggle_right, LOW);
}

void all_off() {
  digitalWrite(toggle_left, LOW);
  digitalWrite(toggle_right, LOW);
}

void forward(int len) {
  left_forward();
  right_forward();
  delay(len);
  all_off();
}

void backward(int len) {
  left_backward();
  right_backward();
  delay(len);
  all_off();
}

void clockwise_spin(int len) {
  left_forward();
  right_backward();
  delay(len);
  all_off();
}

void anticlockwise_spin(int len) {
  left_backward();
  right_forward();
  delay(len);
  all_off();
}

void setup() {
  pinMode(toggle_left, OUTPUT);
  pinMode(toggle_right, OUTPUT);
  pinMode(direction_left, OUTPUT);
  pinMode(direction_right, OUTPUT);
  
  delay(1000 * 1);
  
  forward(800);
  backward(300);
//  clockwise_spin(1400);
//  forward(800);
}

void loop() {
  
}
