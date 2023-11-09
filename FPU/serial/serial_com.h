#ifndef SERIAL_COM_H
#define SERIAL_COM_H

#include <stdio.h>
#include "../device_state/device_state.h"

#define PORT "/dev/ttyACM0"

void open_serial(void);
void setup_com(void);
int read_data(packet_state *buffer);
void close_serial_connection(void);

#endif