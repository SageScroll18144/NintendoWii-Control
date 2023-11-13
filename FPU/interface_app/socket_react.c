#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include "socket_react.h"
#include "../device_state/device_state.h"

int socketCliente;
struct sockaddr_in servidorAddr;

void build_socket_server(void){
    if ((socketCliente = socket(AF_INET, SOCK_DGRAM, 0)) == -1) {
        perror("Erro ao criar o socket");
        exit(EXIT_FAILURE);
    }

    // Configure o endereço do servidor
    memset(&servidorAddr, 0, sizeof(servidorAddr));
    servidorAddr.sin_family = AF_INET;
    servidorAddr.sin_port = htons(12345); // Substitua pelo número da porta desejado
    servidorAddr.sin_addr.s_addr = inet_addr("127.0.0.1"); // Substitua pelo endereço IP do servidor

}
void send_socket_server(packet_state buffer){
    if (sendto(socketCliente, &buffer, sizeof(buffer), 0, (struct sockaddr*)&servidorAddr, sizeof(servidorAddr)) == -1) {
        perror("Erro ao enviar os dados");
        close(socketCliente);
        exit(EXIT_FAILURE);
    }

    printf("Dados enviados com sucesso.\n");
}

void close_server(void){
    close(socketCliente);
}
