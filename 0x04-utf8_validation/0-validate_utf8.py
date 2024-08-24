#!/usr/bin/python3
''' a method that determines if
a given data set represents a valid UTF-8 encoding.
'''


def validUTF8(data):
    '''func body'''
    byte_count = 0
    for elem in data:
        elem = elem & 0xFF # Ensure elem is a single byte
        if byte_count == 0:
            if elem >> 7 == 0:
                continue
            elif elem >> 5 == 0b110:
                byte_count = 1
            elif elem >> 4 == 0b1110:
                byte_count = 2
            elif elem >> 3 == 0b11110:
                byte_count = 3
            else:
                return False
        else:
            if elem >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
