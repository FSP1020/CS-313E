#  File: Work.py

#  Description: Use binary search and linear search
# to find minimum number of lines needed.

#  Student Name: Samuel Pomajevich

#  Student UT EID: SRP2938

#  Partner Name: Natania Christopher

#  Partner UT EID: nnc476

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/29/2020

#  Date Last Modified: 10/29/2020

import sys

import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  sum = 0
  n = 0
  while v // k ** n != 0:
    sum += v // k ** n
    n += 1
  return sum

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  for v in range(1, n + 1):
    if sum_series(v, k) >= n:
      return v
  return 0

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
  low = 0
  high = n
  while low <= high:
    mid = (low + high) // 2
    if sum_series(mid, k) >= n and sum_series(mid - 1, k) < n:
      return mid
    elif sum_series(mid, k) >= n:
      high = mid
    else:
      low = mid
  return 0

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()