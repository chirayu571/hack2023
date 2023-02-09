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



