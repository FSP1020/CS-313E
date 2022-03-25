# File: Fibonacci.py

# Description: Calculates and displays fibonacci series in terms of 1s and 0s.

# Date Created: 10/8/2020

# Date Last Modified: 10/8/2020

# Input: n a positive integer
# Output: a bit string
def f(n):
	bit_list = ['0', '1']
	if n == 0:
		return '0'
	for i in range(1, n):
		bit_list.append(bit_list[i] + bit_list[i-1])
	return bit_list[-1]

# Input: s and p are bit strings
# Output: an integer that is the number of times p occurs in s
def count_overlap (s, p):
	count = 0
	if len(s) < len(p):
		return 0
	for i in range(len(s) - len(p) + 1):
		if s[i : i + len(p)] == p:
			count += 1
	return count


def main():
  # read n and p from standard input
  n = int(input())
  p = input()
  # compute the bit string f(n)
  s = f(n)
  # determine the number of occurrences of p in f(n)
  overlap = count_overlap(s, p)
  # print the number of occurrences of p in f(n)
  print(overlap)

if __name__ == "__main__":
  main()
