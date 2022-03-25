
#  File: Triangle.py

#  Description: Find larget path sum of a triangle using different search
# methods and timing them.

#  Student Name: Samuel Pomajevich

#  Student UT EID: SRP2938

#  Partner Name: Natania Christopher

#  Partner UT EID: nnc476

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/26/2020

#  Date Last Modified: 10/26/2020

import sys

from timeit import timeit

def add(grid, sums, path_sum, row = 0, col = 0):
  if row == len(grid):
    sums.append(path_sum)
  else:
    path_sum += grid[row][col]
    return add(grid, sums, path_sum, row + 1, col) or add(grid, sums, path_sum, row + 1, col + 1)


# returns the greatest path sum using exhaustive search
def brute_force (grid):
  sums = []
  path_sum = 0
  add(grid, sums, path_sum)
  return max(sums)

# returns the greatest path sum using greedy approach
def greedy (grid):
  col = 0
  sum1= 0
  for row in range(len(grid) - 1):
    sum1 += grid[row][col]
    if (grid[row + 1][col] > grid[row + 1][col + 1]):
      col = col
    else:
      col += 1
  sum1 += grid[row + 1][col]
  return sum1

def helper_divide(grid, counter, sum_list):
  if len(grid) == 1:
    sum_list.append(counter + grid[0][0])
  else:
    triangle1 = []
    triangle2 = []
    for line in grid[1:]:
      triangle1.append(line[1:])
      triangle2.append(line[:-1])
    counter += grid[0][0]
    return (helper_divide(triangle1, counter, sum_list)) or (helper_divide(triangle2, counter, sum_list))


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
  counter = 0
  sum_list = []
  helper_divide(grid, counter, sum_list)
  return max(sum_list)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    # loop for bottom-up calculation 
    for i in range(len(grid)-2, -1, -1): 
        for j in range(i+1):  
            if (grid[i+1][j] > grid[i+1][j+1]): 
                grid[i][j] += grid[i+1][j] 
            else: 
                grid[i][j] += grid[i+1][j+1] 
  
    # return the top element 
    # which stores the maximum sum 
    return grid[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]


  return grid


def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  # output greatest path from exhaustive search
  print('The greatest path sum through exhaustive search is')
  print(brute_force(grid))


  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print('The time taken for exhaustive search in seconds is')
  print(times)
  print()

  # output greatest path from greedy approach
  print('The greatest path sum through greedy search is')
  print(greedy(grid))


  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print('The time taken for greedy approach in seconds is')
  print(times)
  print()

  # output greatest path from divide-and-conquer approach
  print('The greatest path sum through recursive search is')
  print(divide_conquer(grid))

  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print('The time taken for recursive search in seconds is')
  print(times)
  print()

  # output greatest path from dynamic programming
  print('The greatest path sum through dynamic programming is')
  print(dynamic_prog(grid))

  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print('The time taken for dynamic programming in seconds is')
  print(times)


if __name__ == "__main__":
  main()

