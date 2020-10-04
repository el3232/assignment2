#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    serverSocket.bind(("", port))
    #Fill in start
    serverSocket.listen(1)
    #Fill in end

    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() #info from ln6
        try:
            message = connectionSocket.recv(2048).decode() #filled in line, inputting msg from client
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read() #filled in line

            #Send one HTTP header line into socket
            #Fill in start - need to return a msg from server socket to client
            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode()) # tells client you have a good conn, webpage can be viewed
            connectionSocket.send(outputdata.encode()) # anytime you send, must encode
            #Fill in end

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            # Send response message for file not found (404)
            # Fill in start
            connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode()) # tells client you have a bad conn, webpage can't be viewed

            # Fill in end

            # Close client socket
            # Fill in start
            connectionSocket.close()
            # Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
