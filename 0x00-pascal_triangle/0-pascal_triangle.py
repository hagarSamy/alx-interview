#!/usr/bin/python3
"""
handling pascal's triangle function
"""


def pascal_triangle(n):
    '''a function to output pascals triangle'''

    myList = []

    if (n <= 0):
        return myList

    myList.append([1])

    i = 1
    while i < n:
        row = [1]
        j = 1
        while j < i:
            row.append(myList[i - 1][j - 1] + myList[i - 1][j])
            j += 1
        row.append(1)
        myList.append(row)
        i += 1
    return myList
