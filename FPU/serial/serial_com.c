#include <fcntl.h> 
#include <termios.h> 
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include "serial_com.h"
#include "../device_state/device_state.h"

int serialPort;
struct termios serialOptions;

void open_serial(void){
    serialPort = open(PORT, O_RDWR | O_NOCTTY); 
    if (serialPort < 0) { 
        printf("Falha na abertura da porta %s\n", PORT); 
        exit(1);
    }
    else printf("Abertura da porta %s!\n", PORT);
}

void setup_com(void){
    tcgetattr(serialPort, &serialOptions);

    // Configure as opções da porta serial
    cfsetispeed(&serialOptions, B115200); // Taxa de baud de entrada
    cfsetospeed(&serialOptions, B115200); // Taxa de baud de saída
    serialOptions.c_cflag |= (CLOCAL | CREAD); // Habilitar leitura e ignorar controle de modem
    serialOptions.c_cflag &= ~PARENB; // Desabilitar paridade
    serialOptions.c_cflag &= ~CSTOPB; // 1 stop bit
    serialOptions.c_cflag &= ~CSIZE; // Limpar bits de tamanho de caractere
    serialOptions.c_cflag |= CS8; // Configurar para 8 bits de dados
    tcsetattr(serialPort, TCSANOW, &serialOptions);
}

int read_data(packet_state *buffer){
    return read(serialPort, buffer, sizeof(packet_state)); 
}

void close_serial_connection(void){
    close(serialPort); 
}