#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 9
OneWire oneWire(ONE_WIRE_BUS);

//DallasTemperature sensors(&oneWire);

#define trigPin D4
#define echoPin D5

long duration;
int distance;


void setup() {
Serial.begin(9600);
 // put your setup code here, to run once:
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);

//sensors.begin();

}



void loop() {
  // put your main code here, to run repeatedly:


//Serial.print("temperature: ");
//sensors.requestTemperatures();
//Serial.println(sensors.getTempCByIndex(0));

digitalWrite(trigPin, LOW);
delayMicroseconds(2);

digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

duration = pulseIn(echoPin, HIGH);
distance = (duration*.0343)/2;
Serial.print("Distance: ");
Serial.println(distance);
delay(2000);

}
