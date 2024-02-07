#ifndef DEVICE_STATE_H
#define DEVICE_STATE_H

#include <stdbool.h>

typedef struct{
    float angle_width, angle_height;
    char direction;
    bool shot;
}packet_state;

#endif