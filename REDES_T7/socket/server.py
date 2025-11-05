import socket

# Configurações do servidor
HOST = 'localhost'
PORT = 12345

# Inicializa o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket à porta
server_socket.bind((HOST, PORT))

# Escuta por conexões
server_socket.listen(1)

print(f'Servidor escutando em {HOST}:{PORT}')

# Aceita a conexão
conn, addr = server_socket.accept()
print('Conectado por', addr)

while True:
    # Recebe os dados do cliente
    data = conn.recv(1024)
    if not data:
        break
    print('Cliente:', data.decode())

    # Envia uma mensagem de volta para o cliente
    message = input('Digite sua resposta: ')
    conn.sendall(message.encode())

# Encerra a conexão
conn.close()
