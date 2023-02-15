from socket import *
from Part1 import *

serverPort = 12404
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",serverPort))

serverSocket.listen(1)

while (1):
    connectionSocket,address = serverSocket.accept()
    # receive dat file

    data = b''
    while (1):
        chunk = connectionSocket.recv(4096)
        if not chunk:
            break

        data += chunk
        
        with open('EncryptedData.dat', 'wb') as file:
            file.write(data)
        
    # bruteforce the encryption and decrypt data file

        with open('EncryptedData.dat', 'rb') as file:
            data2 = file.read()

        
        encryptedMessage = data2.decode()
        
        railFenceKey = 2 # rail fence uses 2 as minumum key.
        crackedKey = False
        

        recognizable_text = ["Rowley","Trinidad","Tobago","murders","Minister","Keith"]
        test = [False,False,False,False,False,False]

        while crackedKey == False:
            caesarCipherKey = 0
            while (crackedKey == False) and caesarCipherKey < 127:

                decryptedMessage = doubleCipherDecrypt(encryptedMessage,caesarCipherKey,railFenceKey)
                
                for i in range(len(recognizable_text)):
                    if recognizable_text[i] in decryptedMessage:
                        test[i] = True
            
                if test[0] == True or test[1] == True or test[2] == True or test[3] == True or test[4] == True or test[5] == True:
                    crackedKey = True
                    foundcaesarCipherKey = caesarCipherKey
                    foundrailFenceKey = railFenceKey
            
                caesarCipherKey = caesarCipherKey + 1
        
            railFenceKey = railFenceKey + 1

        print("Key for Rail Fence Cipher found using brute Force method:" + str(foundrailFenceKey))
        print("Key for Caesar Cipher found using brute Force method:" + str(foundcaesarCipherKey))
        
        print(decryptedMessage)
    connectionSocket.close()


