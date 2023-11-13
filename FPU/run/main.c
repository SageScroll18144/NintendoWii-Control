#include <stdio.h>
#include "../serial/serial_com.h"
#include "../device_state/device_state.h"
#include "../interface_app/socket_react.h"

int main(){
    packet_state data_received_from_ESP;

    //setup
    open_serial();
    setup_com();
    build_socket_server();

    //loop
    while(1){
        read_data(&data_received_from_ESP);
        printf("Axis: %c | Trigger: %s\n", data_received_from_ESP.direction, (data_received_from_ESP.shot) ? "shot" : "hold");
        send_socket_server(data_received_from_ESP);
    }

    close_serial_connection();
    close_server();
    return 0;
}