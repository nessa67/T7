import socket

# Configurações do servidor
HOST = 'localhost'
PORT = 12345

# Inicializa o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client_socket.connect((HOST, PORT))

while True:
    # Solicita ao usuário que digite uma mensagem
    message = input('Digite sua mensagem: ')

    # Envia a mensagem para o servidor
    client_socket.sendall(message.encode())

    # Recebe a resposta do servidor
    data = client_socket.recv(1024)
    print('Servidor:', data.decode())

# Encerra a conexão
client_socket.close()
