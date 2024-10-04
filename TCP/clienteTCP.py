import socket

# Crear socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dirección del servidor
server_address = ("localhost", 12345)

print("Conectando al servidor...")
client_socket.connect(server_address)
print("Conectado al servidor")

# Enviar mensaje
client_socket.send(b"Hola servidor, soy el cliente")

# Recibir respuesta
response = client_socket.recv(1024)
print(f"Respuesta del servidor: {response.decode()}")

# Cerrar conexión
client_socket.close()
