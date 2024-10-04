import socket

# Crear un socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar mensaje al servidor
server_address = ("localhost", 12345)
client_socket.sendto(b"Hola servidor", server_address)

# Recibir respuesta
response, _ = client_socket.recvfrom(1024)
print(f"Respuesta del servidor: {response.decode()}")
