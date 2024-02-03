#include <Arduino.h>
#include <esp_now.h>
#include <WiFi.h>
#include "accelerometer.h"
#include "device_state.h"
#include "trigger_gun.h"

#define MODE 1 //0 -> Board  | 1 -> Control | 2 -> Debug

uint8_t broadcastAddress[] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};
esp_now_peer_info_t peerInfo;

void setup() {
  Serial.begin(115200);
  if(MODE){
    buildAccelerometer();
    buildTrigger();
  }
  
  WiFi.mode(WIFI_STA);
  // Init ESP-NOW
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  // Once ESPNow is successfully Init, we will register for Send CB to
  // get the status of Trasnmitted packet
  esp_now_register_recv_cb(OnDataRecv);
  esp_now_register_send_cb(send_espnow_packet);

  // Register peer
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;  
  peerInfo.encrypt = false;
  
  // Add peer        
  if (esp_now_add_peer(&peerInfo) != ESP_OK){
    Serial.println("Failed to add peer");
    return;
  }
}

void loop() {
  switch (MODE){
    case 1:
      packet_state state;
      state.direction = getAxis();
      state.shot = readTrigger();

      Serial.print("---------------\nDirection read: "); Serial.println(state.direction);
      Serial.print("Shot read: "); Serial.print(state.shot);Serial.println("\n---------------");

      esp_err_t result = esp_now_send(broadcastAddress, (uint8_t *) &state, sizeof(state));
    break;
    case 2:
      debugAxis();
    break;
    default:
    break;
  }

}