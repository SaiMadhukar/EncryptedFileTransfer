
import socket
import threading
import os
from Crypto.Cipher import AES
import base64

key = "This is a key123"
iv = "This is an IV456"
obj = AES.new(key, AES.MODE_CBC, iv)

def RetrFile(name, sock):
    lineNo = 0
    filename = sock.recv(1024)
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = sock.recv(1024)
        if userResponse[:2] == 'OK':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                print(lineNo," original Data:",bytesToSend)
                lineNo += 1
                #encryptedBase64Data = base64.b64encode(obj.encrypt(bytesToSend))
#                cipherText = obj.encrypt(bytesToSend)
# print("encryptedBase64Data Data:",cipherText)

                sock.send(bytesToSend)
                i=0
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    print(lineNo," original Data:",bytesToSend)
                    lineNo += 1
                    print()
                    #encryptedBase64Data = base64.b64encode(obj.encrypt(bytesToSend))
                    #print("encryptedBase64Data Data:",encryptedBase64Data)
#                    cipherText = obj.encrypt(bytesToSend)
#                 print("encryptedBase64Data Data:",cipherText)
                    sock.send(bytesToSend)
        sock.close()
    else:
        sock.send("ERR ")

    sock.close()

def Main():
    host = ''
    port = 5000

    s = socket.socket()
    s.bind((host,port))
    s.listen(5)

    
    
    
    print "Server Started."
    while True:
        c, addr = s.accept()
        print("client connedted ip:<" + str(addr) + ">")
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()

    s.close()

if __name__ == '__main__':
    Main()
