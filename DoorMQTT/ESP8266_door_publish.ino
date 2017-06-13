/*
 Create by Carmelito for the Upcycled Clock project to send an MQTT message from ESP8266 to the Intel Edison
 Date :06-08-2017
 For more details on setting up ESP8266 breakout board checkout -https://learn.adafruit.com/adafruit-huzzah-esp8266-breakout
*/

#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// Update your WiFi router details below
const char* ssid = "XXXXXXXXX";
const char* password = "XXXXXXXXXXXX";
const char* mqtt_server = "test.mosquitto.org";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;
int doorPin = 13;//Magnetic contact switch aka door sensor
int ledPin =2;//Blue Led on the ESP8266 Huzzah board

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void reconnect() {
  // Loop until  connected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // once connected ,publishing a test message to the door topic
      client.publish("door", "connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(doorPin, INPUT_PULLUP);
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  digitalWrite(ledPin, LOW);
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  long now = millis();
  if (now - lastMsg > 10000) { //Change this to 30 seconds
    lastMsg = now;
    ++value;
      if(digitalRead(13) == LOW) //door is open
      {
      digitalWrite(ledPin, HIGH);
      Serial.println("Publish message: closed ");
      client.publish("door", "closed");
      }
      else //door is closed
      {
        digitalWrite(ledPin, LOW);
       Serial.println("Publish message:open ");
       client.publish("door", "open");
      }

  }
}
