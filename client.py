
import socket
from Crypto.Cipher import AES
import base64

key = "This is a key123"
iv = "This is an IV456"
obj = AES.new(key, AES.MODE_CBC, iv)

def Main():
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.connect((host, port))
    lineNo = 0

    filename = raw_input("Filename? -> ")
    if filename != 'q':
        s.send(filename)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])
            message = raw_input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
            if message == 'Y':
                s.send("OK")
                f = open('new_'+filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)


                #print("Recieved Data:",data)
                # decDataLen = base64.b64decode(data)
                #print("After Decoding data len:",len(decDataLen))
                #decryptedData = obj.decrypt(decDataLen)


                print(lineNo," Before Decrypting Data:",data)
#                plainText = obj.decrypt(data)
#                print(lineNo," Before Decrypting Data:",plainText)
                lineNo += 1
                f.write(data)
                i = 0
                while totalRecv < filesize and len(data) > 0:

                    #print("Still Remaining to Download",(filesize - totalRecv))
                    data = s.recv(1024)
                    totalRecv += len(data)
                    print(lineNo,"Before Decrypting Data Data:",data)
#                    print()
#                    plainText = obj.decrypt(data)
#
#                    # decDataLen = base64.b64decode(data)
#                    # #print("After Decoding data len:",len(decDataLen))
#                    # decryptedData = obj.decrypt(decDataLen)
#                    # print(lineNo," After Decrypting Data:",decryptedData)
#                    print(lineNo," After Decrypting Data:",plainText)

                    lineNo += 1
                    f.write(data)


                    #print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"
                print "Download Complete!"
                f.close()
        else:
            print "File Does Not Exist!"

    s.close()


if __name__ == '__main__':
    Main()
