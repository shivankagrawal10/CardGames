import socket
import sys

class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()    # For this to work on your machine this must be equal to the ipv4 address of the machine running the server
                                            # You can find this address by typing ipconfig in CMD and copying the ipv4 address. Again this must be the servers
                                            # ipv4 address. This feild will be the same for all your clients.
        #self.client.setblocking(1)
        self.port = 5556
        self.addr = (self.host, self.port)
        self.id = int(self.connect())

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    def close(self):
        print("Connection Closed",file=sys.stderr)
        self.client.close()

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            return self.client.send(str.encode(data))
            #reply = self.client.recv(2048).decode()
            #return reply
        except socket.error as e:
            return str(e)
    
    def receive(self):
        """
        :param none
        :return: str
        """
        ex = self.client.recv(2048).decode('UTF-8')
        #while ex!= b'':
        #    ex += self.client.recv(2048).decode('UTF-8')
        return ex