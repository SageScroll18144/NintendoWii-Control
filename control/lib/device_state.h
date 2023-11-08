#ifndef DEVICE_STATE_H
#define DEVICE_STATE_H

typedef struct{
    char direction;
    bool shot;
}packet_state;

void send_packet(char direction, bool shot);

#endif 