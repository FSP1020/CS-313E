#!/bin/python3

import os
import re
import sys
import math

# Enter your code here. Read input from STDIN. Print output to STDOUT
# gets the greatest sum of all the paths in the grid
def path_sum(grid, n):
    if n == 0:
        return grid[m][n]
    else:
        return grid[m][n] + min( path_sum(grid, m-1, n-1), path_sum(grid, m-1, n), path_sum(grid, m, n-1) )


def main():
    # read data from standard input
    n = int(input())
    # read the dimension of the grid and the grid itself
    grid = []
    rows_of_grid = []
    for row in range(n):
        if row != 0:
            grid.append(rows_of_grid)
        rows_of_grid = []
        row = input().split()
        for col in range(n):
            rows_of_grid.append(int(row[col]))
    # get the greatest path sum in the grid and print
    print(path_sum(grid, n))

if __name__ == "__main__":
    main()