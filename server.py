import socket as s

# server info
hostIP, port = s.gethostname(), 5055

bufferSize = 1024  #1B of info

#### CONFIGURATION ####
serverSocket = s.socket()    # socket inst for server
serverSocket.bind((hostIP, port))
serverSocket.listen()

#### serving client ####

def acceptClient():
    print("server is live...")
    clientSocket, clientInfo = serverSocket.accept()      # client tings
    print("connected to {}".format(clientInfo[0]))
    info = clientSocket.recv(bufferSize)   # client's info 
    print(info)
    if info:
        print("info received successfully:)")
        print(info)
    else:
        print("something wrong happend.")


if __name__ == "__main__":
    while True:
        acceptClient()

