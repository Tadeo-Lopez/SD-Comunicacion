import socket

# Crear socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar socket a IP y puerto
server_socket.bind(("localhost", 12345))

# Escuchar conexiones entrantes
server_socket.listen(5)
print("Servidor TCP esperando conexiones...")

while True:
    print("Esperando conexión...")
    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida con {client_address}")
    
    # Recibir mensaje
    message = client_socket.recv(1024).decode()
    print(f"Mensaje recibido: {message}")
    
    # Enviar respuesta
    client_socket.send(b"Mensaje recibido correctamente")
    
    # Cerrar la conexión
    client_socket.close()
