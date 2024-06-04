#include <ESP8266WiFi.h>
#include <Servo.h>

Servo myservo;  // Create servo object to control a servo

void setup() {
  myservo.attach(D6);  // Attaches the servo on D6 to the servo object
}

void loop() {
  myservo.write(0);    // Set servo to 0 degrees
  delay(500);        // Wait for 20 seconds
  
  myservo.write(45);   // Set servo to 45 degrees
  delay(500);        // Wait for 20 seconds

  myservo.write(90);   // Set servo to 90 degrees
  delay(500);        // Wait for 20 seconds

  myservo.write(135);  // Set servo to 135 degrees
  delay(500);        // Wait for 20 seconds

  myservo.write(180);  // Set servo to 180 degrees
  delay(500);        // Wait for 20 seconds
}
