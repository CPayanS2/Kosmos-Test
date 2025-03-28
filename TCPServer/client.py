import socket, threading

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
        self.client.connect((self.host, self.port))
        self.username = input("nombre para el cliente: ")
        print(f"Cliente conectando a: {self.host}:{self.port}...")

    def receiveMsg(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'username':
                    self.client.send(self.username.encode('utf-8'))
                else:
                    print(f"Servidor dice: {message}")
            except:
                self.client.close()
                break

    def writeMsg(self):
        while True:
            message = input("Msg:")
            self.client.send(message.encode('utf-8'))
            if message == 'DESCONEXION':
                self.client.close()
                break

    def run(self):
        receiveTh = threading.Thread(target=self.receiveMsg)
        receiveTh.start()
        sendTh = threading.Thread(target=self.writeMsg)
        sendTh.start()

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    client = Client(host, port)
    client.run()
