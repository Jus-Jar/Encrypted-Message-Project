# INFO 2604 Assignment 1
# Group Members:
#Jared Heeralal (816030252)
#Dillan Parmanan ()

# helper functions
def charArrayToString(arr):
    result = ""
 
    # traverse char array and append  characters to result string
    for x in arr:
        result += str(x)
 
    # return string
    return result

#encryption functions

# accepts a message (string) and the key (int) for the rail fence encryption
def railFenceEncrypt(message,key):

    # creates a n-D array where key determines the value of n. Values are initialized to NULL 
    rail = [['\0' for i in range(len(message))] for j in range(key)]
    result = []

    message_length = len(message)

    #to find the direction 
    row = 0
    col = 0;
    switch_row = False

    for i in range(message_length):

        # Switches the direction of the traversal of rows when current row is the top or bottom row 
        if (row == 0) or (row == key -1):
            switch_row = not switch_row # toggles between true and false

        #adds a char from the string into an array location, increments the column
        rail[row][col] = message[i]
        col += 1

        # increments the row if switch_row is true (traversing rows downwards)
        if switch_row == True:
            row += 1
        
        # decrements the row if switch_row is false (traversing rows upwards)
        else: 
            row = row - 1

    # reads characters row by row and store in result array
    for i in range (key):
        for j in range (message_length):
            # skips empty array locations
            if rail[i][j] != "\0":
                result.append(rail[i][j]) #adds characters to result array

    # for i in rail:
    #     print(i)

    return charArrayToString(result)


def caesarCipherEncrypt(message, key):
    
    result = ""

    for char in message:
        charAsciiValue = ord(char) # ord() returns the unicode from a given character
        shiftedCharAsciiValue = (charAsciiValue + key) % 128
        result += chr(shiftedCharAsciiValue) #chr returns the string value of a unicode integer

    return result
    

# decryption functions
def railFenceDecrypt(message, key):
    rail = [['\0' for i in range(len(message))] 
            for j in range(key)] 
  
    # to find the direction 
    switch_row = None
    row = 0
    col = 0
      
    for i in range(len(message)): 
        if row == 0: 
            switch_row = True
        if row == key - 1: 
            switch_row = False
              
        rail[row][col] = '*'
        col += 1
          
        if switch_row: # determines if to traverse down rows or traverse up the rows
            row += 1
        else: 
            row -= 1



    index = 0
    for i in range(key): 
        for j in range(len(message)): 
            if ((rail[i][j] == '*') and (index < len(message))): 
                rail[i][j] = message[index] 
                index += 1

    # for i in rail:
    #     print(i)
    result = [] 
    row = 0
    col = 0
    for i in range(len(message)): 
          
        if row == 0: 
            switch_row = True
        if row == key - 1: 
            switch_row = False
              
        if (rail[row][col] != '\n'): 
            result.append(rail[row][col]) 
            col += 1
              
        if switch_row: 
            row += 1
        else: 
            row -= 1

    return charArrayToString(result)

# def railFenceDecrypt(message,key):
    
#     rail = [['\0' for i in range(len(message))] for j in range(key)]
#     m = 0 # char count for message
#     init = 0

#     # Reforms message as a rail cipher using a n-D array where n is the key
#     for j in range(key):

#         for i in range(init,len(message),key+1):
#             rail[j][i] = message[m]
#             m +=1 # increments the character in the string to b added to rail

#         init +=1

#     for i in rail:
#         print(i)

#     row = 0
#     col = 0;
#     switch_row = False
#     result =[]

#     for i in range(len(message)):
        
#         # Switches the direction of the traversal of rows when current row is the top or bottom row 
#         if (row == 0) or (row == key -1):
#             switch_row = not switch_row # toggles between true and false

#         if rail[row][col] != "\0":
#             result.append(rail[row][col])
            
#         col += 1

#         # increments the row if switch_row is true (traversing rows downwards)
#         if switch_row == True:
#             row += 1
        
#         # decrements the row if switch_row is false (traversing rows upwards)
#         else: 
#             row = row - 1    
    
#     return charArrayToString(result)

def caesarCipherDecrypt(message, key):
    result  = ""
    for char in message:
        charAsciiValue= ord(char) # ord() returns the unicode from a given character
        shiftedCharAsciiValue = (charAsciiValue - key) % 128
        result += chr(shiftedCharAsciiValue) #chr returns the string value of a unicode integer
    return result

def doubleCipherEncrypt(message,key1,key2):

    encryptedMessage = railFenceEncrypt(message,key1)
    encryptedMessage = caesarCipherEncrypt(encryptedMessage,key2)

    return encryptedMessage 

def doubleCipherDecrypt(encryptedMessage,key1,key2):

    decryptedMessage = caesarCipherDecrypt(encryptedMessage,key1)
    decryptedMessage = railFenceDecrypt(decryptedMessage,key2)

    return decryptedMessage 


#######################################
# main code

# Rail fence encrypt test
# e_msg = railFenceEncrypt("Hello Class",2)
# print("Rail Fence encrypted message:")
# print(e_msg)

# # Rail fence decrypt test
# print("Rail Fence decrypted message:")
# print(railFenceDecrypt(e_msg,2))


# # caesar cipher encrypt test
# print("Caesar cipher encrypted message:")
# print(caesarCipherEncrypt(e_msg,1))

# # caesar cipher decrypt test
# print("Caesar cipher encrypted message:")
# d_e_msg = caesarCipherEncrypt(e_msg,1)
# print(d_e_msg)
# print("Caesar cipher decrypted message:")
# result = caesarCipherDecrypt(e_msg,1)
# print(result)
# f_result = railFenceDecrypt(e_msg,2)
# print("Final Result:")
# print(f_result)

# print("**************************")
# msg = "Hello Class my name is Jared.\n How are you?"
# msg = msg.replace("\n"," ")
# print(msg)
# print("**************************")
# e = doubleCipherEncrypt(msg,3,6)
# print(e)
# d = doubleCipherDecrypt(e,6,3)
# print(d)