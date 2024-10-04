import socket

# Crear socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Dirección del servidor
server_address = ("localhost", 12345)

# Enviar petición al servidor
client_socket.sendto(b"Hola servidor, soy el cliente", server_address)

# Recibir respuesta del servidor
response, _ = client_socket.recvfrom(1024)
print(f"Respuesta del servidor: {response.decode()}")

# Enviar confirmación de recibido al servidor
client_socket.sendto(b"Confirmacion recibida", server_address)

# Recibir confirmación final del servidor
final_ack, _ = client_socket.recvfrom(1024)
print(f"Confirmación final del servidor: {final_ack.decode()}")

client_socket.close()
