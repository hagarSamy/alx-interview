#!/usr/bin/python3
"""
island_perimete
"""


def island_perimeter(grid):
    '''calc the perimeter of an island'''
    grid_len = len(grid)
    row_len = len(grid[0])
    perim = 0
    for i in range(grid_len):
        for j in range(row_len):
            if grid[i][j] == 1:
                if perim == 0:
                    perim = 4
                perim += 2
    return perim
