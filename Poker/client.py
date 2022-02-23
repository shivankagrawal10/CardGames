import socket
import sys

'''# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 5555

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
tm = s.recv(1024)                                     

#s.close()

print("The time got from the server is %s" % tm.decode('ascii'))'''

host = socket.gethostname()    
port = 5556                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    print("Enter Player Name: ",file=sys.stderr)
    name = input()
    s.send(str.encode(name))
    #data = s.recv(2048)
    #s.close()
    #print('Received', repr(data))