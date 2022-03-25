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

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
    # use binary search here
    low = 0
    high = n
    while low <= high:
        mid_value = (low + high) // 2
        if sum_series(mid_value, k) >= n and sum_series(mid_value - 1, k) < n:
            return mid_value
        elif sum_series(mid_value, k) >= n:
            high = mid_value
        else:
            low = mid_value
    return 0 

def main(params):
    n = params[0]
    k = params[1]
    return binary_search(n, k)

if __name__ == "__main__":
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  inpt = sys.stdin.read().split()
  params = (int(inpt[0]), int(inpt[1]))
  fptr.write(str(main(params)))
  fptr.close()