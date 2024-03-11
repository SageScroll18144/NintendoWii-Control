# lib

Biblioteca desenvolvida para a manipulação do device.

## accelerometer

```c
void buildAccelerometer(void);
```

- Pre-configura o acelerômetro.

```c
char sideAxis(void);
```

- Retorna o lado que está apontando (F, R, L, D, U).

```c
float getAxisY(void);
```

- Retorna um valor real da aceleração no eixo Y.

```c
float getAxisZ(void);
```

- Retorna um valor real da aceleração no eixo Z.

```c
void debugAxis(void);
```

- Retorna um valor real da aceleração no eixo X.

## trigger

Gatilho do device.

```c
void buildTrigger(void);
```

- Pre-configura o gatilho.

```c
bool readTrigger(void);
```

- Retorna a leitura do gatilho.

## device_state

```c
typedef struct{
    float angle_width, angle_height;
    char direction;
    bool shot;
}packet_state;
```
- Struct enviada via _espnow_ para descrever o estado do device. Contêm os valores reais lidos em dois eixos(associado com a largura e altura da tela; direção e se o usuário ativou o gatinho).


```c
void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len);
```

- Callback da esp

```c
void send_espnow_packet(const uint8_t *mac_addr, esp_now_send_status_t status);
```

- Função de envio via _espnow_

### Obs.:

O device é constituido de duas ESPs, uma transceiver e outra receiver. Sobre a ESP receiver, ela serve como um gateway, recebendo _espnow_ e enviando via serial para o computador embarcado. Vale salientar que foi critério do projetista implementar um seletor para determinar se o Rx deve mandar um caracter(1 byte) ou a struct de estado do equipamento.

## MODOS DE OPERAÇÃO

```c
#define MODE 0 //0 -> Board  | 1 -> Control | 2 -> Debug
```

- Define o modo de operação da placa.

| Modo  | Deploy |
| ------------- | ------------- |
| 0  | ESP integrada ao computador  |
| 1 | ESP integrada ao controle  |
| 2 | Debug da ESP integrada ao controle  |

```c
#define TYPE_SERIAL_SENDER 1

#define DEBUG_SERIAL 0
#define SENDER_SERIAL_CHAR 1
#define SENDER_SERIAL_STRUCT 2
```

- Modos de operação de envio serial.

| Modo  | Deploy |
| ------------- | ------------- |
| 0  | Debug da ESP integrada ao computador  |
| 1 | Modo de envio de caractere(direção) |
| 2 | Modo de envio de pacote(packet_state) |