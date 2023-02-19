# INFO 2604 Assignment 1
# Jared Heeralal (816030252)
#Dillan Parmanan ()

import json 
from Part1 import * 

# CryptoAnalysis using frequency analysis (ASCII)

# import data from json file

f_data = json.load(open('ascii_freq.json','r'))

for item in f_data:
    print(item['Char'])
    print(item['Freq']) 
    print("\n")

# Could store data in array and sort in asc or desc order according to frequency
def count_letter_frequencies(text):

    frequencies = {}

    for asciicode in range(65,91):
        frequencies[chr(asciicode)] = 0

    for letter in text:
        asciicode = ord(letter.upper())
        if asciicode >= 65 and asciicode <= 90:
            frequencies[char(asciicode)] += 1

    sorted_by_frequency = sorted(frequencies.items(), key = itemgetter(1), reverse=True)

    return sorted_by_frequency

## step 2;
def decrypt_file(filename, filename2, filename3):

    """
    Use the dictionary to decrypt the encrypted file
    and save the result.
    """
    filename = "Rowley.dat"

    with open (filename, "rb") as file:
        encrypted_data  = file.read()
    
    f_data = json.load(open(filename3,'r'))

    decrypted_list = []

    for letter in encrypted_text:
        asciicode = ord(letter.upper())
        if asciicode >= 65 and asciicode <= 90:
            decrypted_list.append(decryption_dict[letter])

    filename3 = "".join(decrypted_list)

    f_data = open(filename3, "w")
    f_data.write(filename3)
    f_data.close()


    try: decrypt_file("Rowley.dat","part3Decrypt.dat","ascii_freq.json")

    except Exception as e:
        print(e)


# find the occurences of all characters in rowley.dat and store in array




## decrypt 


#sort array in same order as data array and then compare the characters

# swap characters with characters in dataset according to positions in array

# decrypt using railfence algorithm