import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
print ("Connecting to server")
s.connect((host, port))                               

# Receive no more than 1024 bytes
#while True :
tm = s.recv(1024)
print ("Receiving from server")
#print("The time got from the server is %s" % tm.decode('ascii'))
                                    

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))
input("Want more?") 