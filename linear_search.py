#!/bin/python3

import os
import re
import sys
import math

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  sum_of_series = 0
  n = 0
  while v // k ** n != 0:
    sum_of_series += v // k ** n
    n += 1
  return sum_of_series

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  for v in range(1, n + 1):
    if sum_series(v, k) >= n:
      return v
  return 0

def main(params):
  params
  n = params[0]
  k = params[1]

  return linear_search(n, k)

if __name__ == "__main__":
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  inpt = sys.stdin.read().split()
  params = (int(inpt[0]), int(inpt[1]))
  fptr.write(str(main(params)))
  fptr.close()