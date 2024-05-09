import socket

def server_program():
    # Obtener el nombre del host
    host = socket.gethostname()
    port = 8082  # Iniciar puerto en un número alto para evitar conflictos

    server_socket = socket.socket()  # Obtener instancia
    server_socket.bind((host, port))  # Enlazar el host y el puerto

    # Configurar cuántos clientes puede escuchar simultáneamente
    server_socket.listen(2)
    conn, address = server_socket.accept()  # Aceptar nueva conexión
    print("Connection from: " + str(address))
    while True:
        # Recibir datos en stream, es decir, en paquetes pequeños
        data = conn.recv(1024).decode()
        if not data:
            # Si no se reciben datos, romper
            break
        print("From connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # Enviar datos al cliente

    conn.close()  # Cerrar la conexión

if __name__ == '__main__':
    server_program()