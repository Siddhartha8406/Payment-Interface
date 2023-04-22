/*
SDA - D4
SCK - D5
MOSI - D7
MISO - D6

GND - GND
RST - D3
3.3V - 3.3V
*/

//RFID Configuration 
#include <SPI.h>
#include <MFRC522.h>
//RFID Wifi
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>


const char* ssid = "WIFI SSID";
const char* password = "WIFI PASSWORF";
String serverName = "http://HOST_IP_ADDRESS/send_card_id/";

constexpr uint8_t RST_PIN = D3;
constexpr uint8_t SS_PIN = D4;

MFRC522 rfid(SS_PIN, RST_PIN);
MFRC522::MIFARE_Key key;

String tag;
String oldID = "111";
void setup() {
  Serial.begin(115200);
  SPI.begin(); // Init SPI bus
  rfid.PCD_Init(); // Init MFRC522

  WiFi.begin(ssid, password);
  delay(2000);
  Serial.println(WiFi.localIP());
  Serial.println("Connected...");
}

void loop() {
  if ( ! rfid.PICC_IsNewCardPresent())
    return;
  if ( ! rfid.PICC_ReadCardSerial())
    return;

  for (byte i = 0; i < 4; i++) {
    tag += rfid.uid.uidByte[i];
  }
  SendAPI(tag);
  tag = "";

}

void SendAPI(String code){
  if(code != oldID){
    oldID = code;
    if(WiFi.status()== WL_CONNECTED){
      int httpResponseCode = 0;
      WiFiClient client;
      HTTPClient http;

      String URL = serverName + code;

      http.begin(client, URL.c_str());

      httpResponseCode = http.GET();
      String payload = http.getString();

      Serial.println(httpResponseCode);
      Serial.println(payload);
    }
  }
}