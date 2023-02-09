# hack2023

#server.py

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


#client.py

import socket as s

# server info
hostIP, port = s.gethostname(), 5055

###### CONFIGURATION ########
serverSocket = s.socket()

try:
    serverSocket.connect((hostIP, port))
except ConnectionRefusedError:
    print("server unavailable !!!!!!!!!!")


class POST:
    def __init__(self, email, phNo, username, password) -> None:
        self.email = email.encode("ascii")
        self.phNo = phNo.encode("ascii")
        self.username = username.encode("ascii")
        self.password = password.encode("ascii")

    def sendInfo():
        print("sending info to server.....")

        INFO = [self.email, self.phNo, self.username, self.password]
        for _ in INFO:
            serverSocket.send(bytes(_))
        print("info sent.")


if __name__ == "__main__":
    demoPOST = POST("ksjdfk", "7556", "asdfadsf", "asdfsadfs")
    demoPOST.sendInfo()



