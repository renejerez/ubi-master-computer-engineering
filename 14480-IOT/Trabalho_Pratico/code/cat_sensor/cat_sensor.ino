#include <Servo.h>

#define trigPin D4
#define echoPin D5
#define servoPin D6

long duration;
int distance;

Servo myservo;
bool catDetected = false;

void setup() {
  Serial.begin(115200);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  myservo.attach(servoPin);
  myservo.write(0);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration * 0.0343) / 2;
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  if (distance < 10 && !catDetected) {
    myservo.write(180);
    delay(2000);  // Wait for 3 seconds
    myservo.write(0);
    catDetected = true;
  } else if (distance >= 10) {
    catDetected = false;
  }

  delay(1000);  // Short delay to avoid rapid looping
}
