# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
# Note: input will never be an empty string

import os

def fake_bin(x):
    bin_string = ''
    for i in x:
        if int(i) < 5:
            bin_string += '0'
        elif int(i) >= 5:
            bin_string += '1'
    print(bin_string)

fake_bin(x = input("Num a ser convertido: "))