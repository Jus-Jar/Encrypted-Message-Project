from socket import *
from random import *
from Part1 import *

serverName = "localhost"
serverPort = 12404

clientSocket = socket(AF_INET,SOCK_STREAM)

clientSocket.connect((serverName,serverPort))



# read data file
filename = "NoMoreMurders.dat"
filename2 = "Rowley.dat"
with open (filename,'rb') as file:
    message = file.read()

key1 = 3 #Rail fence key
key2 =  8 #caesar cipher key

message = message.decode() #converts bytes to string
message = message.replace("\n"," ") #removes newlines from text

encryptedMessage = doubleCipherEncrypt(message,key1,key2)
encryptedMessage = bytes(encryptedMessage,"utf-8") #re-encodes message to be written into Rowley.dat

# encrypt data file and save as Rowley.dat

with open (filename2,'wb') as file:
    file.write(encryptedMessage)

# send message to program B

#reads Rowley.dat for encrypted message
with open (filename2,'rb') as file:
    encryptedMessage = file.read()

clientSocket.send(encryptedMessage) #sends encrypted message to program B


clientSocket.close()

