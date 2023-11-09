#include <stdio.h>
#include "../serial/serial_com.h"
#include "../device_state/device_state.h"

int main(){
    packet_state data_received_from_ESP;

    //setup
    open_serial();
    setup_com();

    //loop
    while(1){
        read_data(&data_received_from_ESP);
        printf("Axis: %c | Trigger: %s\n", data_received_from_ESP.direction, (data_received_from_ESP.shot) ? "shot" : "hold");
    }

    close_serial_connection();

    return 0;
}