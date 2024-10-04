import socket

# Crear un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", 12345))  # Escuchar en el puerto 12345

print("Servidor UDP en espera de mensajes...")

while True:
    # Recibir mensaje
    message, client_address = server_socket.recvfrom(1024)
    print(f"Mensaje recibido: {message.decode()} de {client_address}")
    
    # Enviar respuesta
    server_socket.sendto(b"Mensaje recibido", client_address)
