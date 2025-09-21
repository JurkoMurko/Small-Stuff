void setup() {
  Serial.begin(9600);
  Serial.println("Enter a number to multiply by 2.");
}

char rx_byte = 0;
String rx_str = "";
boolean not_number = false;
int result;

void loop() {
  if (Serial.available() > 0) {    // is a character available?
    rx_byte = Serial.read();       // get the character
    
    if ((rx_byte >= '0') && (rx_byte <= '9')) {
      rx_str += rx_byte;
    }
    else if (rx_byte == '\n') {
      // end of string
      if (not_number) {
        Serial.println("Not a number");
      }
      else {
        // multiply the number by 2
        result = rx_str.toInt() * 2;
        // print the result
        Serial.print(rx_str);
        Serial.print(" x 2 = ");
        Serial.print(result);
        Serial.println("");
        Serial.println("Enter a number to multiply by 2.");
      }
      not_number = false;         // reset flag
      rx_str = "";                // clear the string for reuse
    }
    else {
      // non-number character received
      not_number = true;    // flag a non-number
    }
  } // end: if (Serial.available() > 0)
}
