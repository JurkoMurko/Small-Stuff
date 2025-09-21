#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define max_len 80
String nam = "Laptop";

RF24 radio(7, 8); // CE, CSN
const byte address[6] = "00001";
const byte address2[6] = "00002";

char bite;
String message;

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address2);
  radio.openWritingPipe(address);
}

void loop() { // I could have the size of the messge be brodcast first to increase efficiency
  radio.stopListening();
  if (Serial.available() > 0) {
    bite = Serial.read();
    if (bite != '\n') {
      message += bite;
    } else{
      message = nam + ": " + message;
      char car[max_len];
      message.toCharArray(car, sizeof(car));
      radio.write(&car, sizeof(car));
      Serial.println(message);
      message = "";
      } 
  }
  
  radio.startListening();
  if (radio.available()) {
    char in[max_len];
    radio.read(&in, sizeof(in));
    Serial.println(in);
  }
  delay(10);
} 
