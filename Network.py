import socket
#serialize objects: turn data into bytes so it can send over to the server
import pickle

#creating a class that willl connnect to the server
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.0.27'
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            #decode byte data so client can be assigned value by computer
            return self.client.recv(2048).decode()
        except:
            pass
        #here we will send data and check for success or failures
    def send(self, data):
        try:
            #send byte data
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)

