#ifndef DEVICE_STATE_H
#define DEVICE_STATE_H

#define TYPE_SERIAL_SENDER 1

#define DEBUG_SERIAL 0
#define SENDER_SERIAL_CHAR 1
#define SENDER_SERIAL_STRUCT 2

typedef struct{
    float angle_width, angle_height;
    char direction;
    bool shot;
}packet_state;

void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len);
void send_espnow_packet(const uint8_t *mac_addr, esp_now_send_status_t status);

#endif 