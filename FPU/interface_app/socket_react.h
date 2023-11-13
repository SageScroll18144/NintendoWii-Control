#ifndef SOCKET_REACT
#define SOCKET_REACT

#include "../device_state/device_state.h"

void build_socket_server(void);
void send_socket_server(packet_state buffer);
void close_server(void);
#endif