#include <Arduino.h>
#include <esp_now.h>
#include <WiFi.h>
#include "device_state.h"

packet_state packet;

void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len){
  
  memcpy(&packet, incomingData, sizeof(packet));
  
  switch (TYPE_SERIAL_SENDER)
  {
    case DEBUG_SERIAL:
      Serial.print("---------------\nDirection read: "); Serial.println(packet.direction);
      Serial.print("Shot read: "); Serial.print(packet.shot);Serial.println("\n---------------");
    break;
    
    case SENDER_SERIAL_CHAR:
      if(!packet.shot) packet.direction = 'S';
      Serial.write(packet.direction); 
    break;

    case SENDER_SERIAL_STRUCT:
      Serial.write((uint8_t*)&packet, sizeof(packet)); 
    break;
  }
  delay(10);
}

void send_espnow_packet(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.print("\r\nLast Packet Send Status:\t");
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
}
