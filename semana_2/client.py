import socket

def client_program():
    host = socket.gethostname()  # Como ambos códigos están en la misma máquina
    port = 8082  # Número de puerto del servidor

    client_socket = socket.socket()  # Instancia del socket
    client_socket.connect((host, port))  # Conectar al servidor

    message = input(" -> ")  # Tomar entrada

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # Enviar mensaje
        data = client_socket.recv(1024).decode()  # Recibir respuesta

        print('Received from server: ' + data)  # Mostrar en pantalla
        message = input(" -> ")  # Nueva entrada

    client_socket.close()  # Cerrar la conexión

if __name__ == '__main__':
    client_program()
