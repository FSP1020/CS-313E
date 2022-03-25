
#  File: Grid.py

#  Description: Find greatest path sum in a 
# 2-D grid.

#  Date Created: 10/29/2020

#  Date Last Modified: 10/29/2020

import os
import re
import sys
import math


# counts all the possible paths in a grid 
def count_paths (n):
    numerator = math.factorial((2*(n - 1)))
    denominator_part = math.factorial(n - 1)
    return numerator // (denominator_part * denominator_part)


# gets the greatest sum of all the paths in the grid
def path_sum(grid, n):
	# For 1st column
    for i in range(1, n):
        grid[i][0] += grid[i - 1][0]
 
    # For 1st row
    for j in range(1, n):
        grid[0][j] += grid[0][j - 1]
 
    # For rest of the 2d matrix
    for i in range(1, n):
        for j in range(1, n):
            grid[i][j] +=  max(grid[i - 1][j], grid[i][j - 1])

    return grid[n - 1][n - 1]


    
def main():
  # read the dimension of the grid
  line = sys.stdin.readline()
  line = line.strip()
  dim = int (line)

  # create an empty grid
  grid = []

  # populate the grid
  for i in range (dim):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    row = list (map (int, line))
    grid.append (row)

  '''
  # print the grid
  print (grid)
  '''

  # get the number of paths in the grid and print
  num_paths = count_paths (dim)
  print (num_paths)
  print ()

  # get the maximum path sum and print
  max_path_sum = path_sum (grid, dim)
  print (max_path_sum)

  
if __name__ == "__main__":
    main()
