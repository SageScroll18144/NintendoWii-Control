#include <Arduino.h>
#include "device_state.h"

void send_packet(char direction, bool shot){
    packet_state packet;
    
    packet.direction = direction;
    packet.shot = shot;

    Serial.write((uint8_t*)&packet, sizeof(packet));
    Serial.flush();
}