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
                perim += 4
                if grid[i+1][j] == 1:
                    perim -= 1
                if grid[i-1][j] == 1:
                    perim -= 1
                if grid[i][j-1] == 1:
                    perim -= 1
                if grid[i][j+1] == 1:
                    perim -= 1
    return peri
