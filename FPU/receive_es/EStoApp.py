import socket
import struct

# Defina a estrutura correspondente à enviada pelo cliente em C
struct_format = 'c?'  # char, bool

# Crie um socket UDP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Configure o endereço e a porta do servidor
endereco_servidor = ('0.0.0.0', 12345)  # Use 0.0.0.0 para aceitar conexões de qualquer interface de rede
servidor_socket.bind(endereco_servidor)

print(f"Servidor esperando por dados em {endereco_servidor}")

# Receba os dados e imprima-os
dados, endereco_cliente = servidor_socket.recvfrom(struct.calcsize(struct_format))
dados_desempacotados = struct.unpack(struct_format, dados)

# Imprima os dados recebidos
print("Dados recebidos:")
print(f"Direção: {dados_desempacotados[0]}")
print(f"Tiro: {dados_desempacotados[1]}")

# Feche o socket
servidor_socket.close()
