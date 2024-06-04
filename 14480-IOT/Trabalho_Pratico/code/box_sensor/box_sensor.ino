#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>

#define trigPin D4
#define echoPin D5

//const char* ssid = "";
//const char* password = ""; // Replace with your actual password
const char* ssid = ""; // Replace with your wifi network
const char* password = ""; // Replace with your actual password


const char* mqtt_server = "iot-tg3r2l.a01.euc1.aws.hivemq.cloud"; // HiveMQ Cloud cluster URL
const int mqtt_port = 8883; // Secure MQTT port
const char* mqtt_user = "renejerez"; // Replace with your HiveMQ Cloud username
const char* mqtt_password = ""; // Replace with your HiveMQ Cloud password
const char* mqtt_topic_distance = "sensor/distance"; // Topic to publish distance
const char* mqtt_topic_status = "sensor/box_status"; // Topic to publish box status

long duration;
int distance;
float sendIntervalMinutes = 0.5; // Variable to set the interval in minutes (0.5 minutes = 30 seconds)

WiFiClientSecure espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Configure secure client
  espClient.setInsecure(); // This is fine for testing, but for production, you should use a certificate

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  client.setServer(mqtt_server, mqtt_port);
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ESP8266Client", mqtt_user, mqtt_password)) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

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

  // Send distance data to MQTT broker
  if (WiFi.status() == WL_CONNECTED) {
    char msg[50];
    snprintf(msg, 50, "Distance: %d cm", distance);
    client.publish(mqtt_topic_distance, msg);

    // Send box status based on distance
    const char* status_msg;
    if (distance > 10) {
      status_msg = "almost empty";
    } else {
      status_msg = "box filled";
    }
    client.publish(mqtt_topic_status, status_msg);
  }

  delay(sendIntervalMinutes * 60000); // Delay for the specified interval in minutes
}
