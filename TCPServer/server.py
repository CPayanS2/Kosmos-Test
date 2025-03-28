import socket, threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = {} #Clients List
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"Servidor corriendo en: {self.host}:{self.port}")

    def broadcast(self, msg, client):
        for cli in self.clients:
            if cli == client:
                cli.send(msg.encode('utf-8'))

    def handleMsg(self, client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8').upper()
                if message == "DESCONEXION":
                    self.disconnectClient(client)
                    break
                else:
                    message = message.replace("SERVIDOR", "CLIENTE")
                    self.broadcast(message, client)
            except:
                self.disconnectClient(client)
                break
    
    def receiveConnections(self):
        while True:
            client, address = self.server.accept()
            client.send('username'.encode('utf-8'))
            username = client.recv(1024).decode('utf-8')
            client.send("Conectado al Servidor exitosamente".encode('utf-8'))
            self.clients[client] = username
            print(f"Cliente: {username} conectado desde: {address}")

            clientTh = threading.Thread(target=self.handleMsg, args=(client,))
            clientTh.start()

    def disconnectClient(self, client):
        username = self.clients[client]
        clientD = self.clients.pop(client)
        client.close()
        print(f"Cliente {username} desconectado")

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    server = Server(host, port)
    server.receiveConnections()

