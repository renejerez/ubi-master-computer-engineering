#include <ESP8266WiFi.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <ESP8266HTTPClient.h>  // Include HTTPClient library
#include <Servo.h>  // Include Servo library

#define ONE_WIRE_BUS D1  // Ensure you connect to a valid digital pin
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

#define trigPin D4
#define echoPin D5
#define servoPin D6  // Define the pin for the servo signal

const char* ssid = "ZFT-96WB-2G";
const char* password = "TG4S54Fa6xtf"; // Replace with your actual password

const char* server = "http://api.thingspeak.com/update"; // ThingSpeak server
const char* apiKey = "JL5OUX3SDNI0OKS9"; // Replace with your ThingSpeak Write API Key

long duration;
int distance;
float sendIntervalMinutes = 0.5;  // Variable to set the interval in minutes (0.5 minutes = 30 seconds)

Servo myservo;  // Create servo object to control a servo
unsigned long servoMoveTime = 0;  // Store the time when the servo was moved to 180 degrees
unsigned long servoDurationSeconds = 10;  // Duration to keep the servo at 180 degrees in seconds

void setup() {
  Serial.begin(115200);  // Using a higher baud rate for more accurate serial monitoring
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  myservo.attach(servoPin);  // Attach the servo to the specified pin
  myservo.write(0);  // Initialize the servo at 0 degrees

  sensors.begin();

  // Connect to Wi-Fi
  int attempts = 0;
  const int maxAttempts = 5;  // Try to connect 5 times

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED && attempts < maxAttempts) {
    delay(500);
    Serial.print(".");
    attempts++;
    if (WiFi.status() != WL_CONNECTED) {
      delay(5000); // Add a delay before retrying
      WiFi.begin(ssid, password); // Retry WiFi connection
    }
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("");
    Serial.println("Failed to connect to WiFi after 5 attempts");
  }
}

void loop() {
  // Ultrasonic distance measurement
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

  // Control the servo based on distance
  unsigned long currentMillis = millis();
  if (distance < 15) {
    myservo.write(180);  // Move the servo to 180 degrees
    servoMoveTime = currentMillis;  // Record the time when the servo was moved
  }

  // Check if the specified duration has passed since the servo moved to 180 degrees
  if (servoMoveTime != 0 && (currentMillis - servoMoveTime >= servoDurationSeconds * 1000)) {
    myservo.write(0);  // Move the servo back to 0 degrees
    servoMoveTime = 0;  // Reset the servo move time
  }

  // Send distance data to ThingSpeak
  if (WiFi.status() == WL_CONNECTED) { // Check if Wi-Fi is connected
    WiFiClient client; // Create WiFiClient object
    HTTPClient http; // Declare an object of class HTTPClient

    String url = String(server) + "?api_key=" + apiKey + "&field1=" + String(distance);

    http.begin(client, url); // Specify request destination with WiFiClient
    int httpCode = http.GET(); // Send the request

    if (httpCode > 0) { // Check the returning code
      String payload = http.getString(); // Get the request response payload
      Serial.println(payload); // Print the response payload
    } else {
      Serial.println("Error on HTTP request");
    }

    http.end(); // Close connection
  }

  delay(sendIntervalMinutes * 60000);  // Delay for the specified interval in minutes
}
