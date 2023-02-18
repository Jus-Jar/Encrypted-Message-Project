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

# find the occurences of all characters in rowley.dat and store in array
filename = "Rowley.dat"

with open (filename, "rb") as file:
    data  = file.read()


#sort array in same order as data array and then compare the characters

# swap characters with characters in dataset according to positions in array

# decrypt using railfence algorithm


