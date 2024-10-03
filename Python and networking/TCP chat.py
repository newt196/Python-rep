################## Corrected code that does run ######################
# Server Code

import socket
import threading

# Socket: Helps control the networking portion of the chat client. 
# Threading: Helps manage muptiple users connecting to the server. (will need different clients to test in verbose mode)

# can we further configure the host ip and not use the loopback address. 

host = '127.0.0.1' 
port = 1234

# port does not have to be explained
# interesting to note that we need to run nmap to see if the port is for viewing. 
# I dont see why it wouldnt because if the clients can connect to the ip and port, nmap should be able to. 

# AF_INET address family - Internet, further explaines that the ip in use is ipv4.
# SOCK_STREAM Specifies that TCP is in use for the communication port.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Bind associates the socket with a specific host and port provided in the above.

# further defining who and what connects to the server. 

clients = []
names = []

# not entirely needed but helps provide feedback to who connects to the server.

def broadcast(message):
  for client in clients:
     client.send(message)

# logic to handle users connecting to the server. defining client handle function to run endlessly
# 
def handle(client):
  while True:
    try:
      message = client.recv(1024)
      broadcast(message)
    except:
      index = clients.index(client)
      clients.remove(client)
      client.close()
      Name = Name[index]
      broadcast ('{} left!'.format(Name).encode('ascii'))
      Name.remove(Name)
      break

# ingress and egress

def receive():

  while True:
    client, address = server.accept()

    print("{} has connected".format)(str(address)())
# how do we process the name variable?

    client.send('Nate'.encode('ascii'))
    Name = client.recv(1024).decode('ascii')
    Name.append(Name)
    clients.append(client)

    print("Name is{}" .format(Name))  
    broadcast("{} joined!" .format(nickname).encode('ascii'))
    client.send('Connected to server successfully!' .encode('ascii'))

thread = threading.Thread(target=handle, args=(client,))
thread.start()

# Thing to note
# We can switch this server and port over to UDP if security is a matter or we dont care if connectionless connections are fine
# TCP on port 1234 may be picked up through nmap or network scans.
# Because udp is connectionless the server may not show up on network scans or at the very least show FILTeRED
# Can onyl conifirm when the server is setup and scanned.
# Interesting to note that we can add cyphers to add the securtiy of the server. 

##################End of code for server ############################



# Server Code
import socket
import threading

# important to remember that socket is used to handle the managment of the network connection
# manages network connections

# threading is used to control the various muntiple connections that are used to connect to the server
# needed to manage multiple connections

# Connection info
# need to make sure that this code can be run in an exe form
 host = '127.0.0.1' 
 port = 1234

# need to define the host address and the port that the server will operate on :)

# Initilzaing the server 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# AF_INET= IPV$
# SOCK_STREAM = TCP connection

# bind just contains the port and host information

clients = []
names = []

# Broadcast to all connected users
def broadcast(message):
  for client in clients:
     client.send(message)

# logic behind user messages
def handle(client):
  while True:
    try:
      message = client.recv(1024)
      broadcast(message)
    except:
      index = clients.index(client)
      clients.remove(client)
      client.close()
      Name = Name[index]
      broadcast ('{} left!'.format(Name).encode('ascii'))
      Name.remove(Name)
      break

# ingress and egress
def receive():
  while True:
    client, address = server.accept()
    print("{} has connected".format(str(address)())
# how do we process the name variable?
    client.send('Nate'.encode('ascii')
    Name = client.recv(1024).decode('ascii')
    Name.append(Name)
    clients.append(client)

    print("Name is{}" .format(Name))  
    broadcast("{} joined!" .format(nickname).encode('ascii'))
    client.send('Connected to server successfully!' .encode('ascii'))

   thread = threading.Thread(target=handle, args=(client,))
   thread.start()




# Client code
import socket
import threading

Name = input("Choose your account name: ")
client = socket.socket(socket.AF_inet, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 1234))

def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

##################### Fixed client code ##############################

import socket
import threading

# Choose account name
Name = input("Choose your account name: ")

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 1234))

def receive():
    while True:
        try:
            # Receive message from server
            # If 'NICK', send chosen nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(Name.encode('ascii'))  # Use the chosen account name
            else:
                print(message)
        except:
            # Close connection on error
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(Name, input(''))  # Use the chosen account name
        client.send(message.encode('ascii'))

# Start threads for receiving and writing messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
