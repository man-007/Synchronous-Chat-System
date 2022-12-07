import socket            
 
# create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")           
 
# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.

    c, addr = s.accept()    
    print('Got connection from', addr )
    
    c.send('Connected to server. You can start chatting now'.encode())
    # send a thank you message to the client. encoding to send byte type.
    while True:
        message = c.recv(1024).decode()
        print("(client) ", message)
        if message=="close":
            c.send('Thank you for connecting'.encode())
            break
        print("(server) ", end="")
        servermessage = input()
        print()
        c.send(servermessage.encode())
    


    # Close the connection with the client
    c.close()

    
    # Breaking once connection closed
    break