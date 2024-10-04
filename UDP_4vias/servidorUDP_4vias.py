import socket

# Crear socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", 12345))

print("Servidor UDP (4 vías) esperando mensajes...")

while True:
    # Recibir mensaje del cliente
    message, client_address = server_socket.recvfrom(1024)
    print(f"Mensaje recibido: {message.decode()} de {client_address}")
    
    # Responder al cliente
    server_socket.sendto(b"Mensaje recibido correctamente", client_address)

    # Recibir confirmación del cliente
    ack, client_address = server_socket.recvfrom(1024)
    print(f"Confirmación del cliente: {ack.decode()}")
    
    # Enviar confirmación final al cliente
    server_socket.sendto(b"Comunicacion cerrada", client_address)
