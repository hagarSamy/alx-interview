#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    '''structs the rotation'''
    length = len(matrix)
    row_len = len(matrix[0])
    new = []
    for i in range(length):
        for j in range(i, row_len):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for row in matrix:
        row.reverse()
