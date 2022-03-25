#  File: MagicSquare.py

#  Description: Given n, find all perfect squares of size n x n.

#  Date Created: 10/18/2020

#  Date Last Modified: 10/19/2020

# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def is_magic (a):
  n = int(len(a) ** (1/2))
  success = int(n * (n**2 + 1) / 2)
  count = 0
  for i in range(0, len(a), n):
    if sum(a[i : i + n]) != success:
      return False

  for j in range(n):
    sum1 = 0
    count = 0
    for l in range(n):
      sum1 += a[j + count]
      count += n
    if sum1 != success:
      return False

  sum1 = 0
  for d in range(0, len(a), n + 1):
    sum1 += a[d]
  if sum1 != success:
    return False

  sum1 = 0
  for f in range(n - 1, len(a) - n + 1, n - 1):
    sum1 += a[f]
  if sum1 != success:
    return False

  return True


# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# it stores all 1-D lists that are magic in the list all_magic
def permute ( a, idx, all_magic ):
  if idx >= len(a):
    all_magic.append(a[:])
  else:
    for i in range(idx, len(a)):
      a[i], a[idx] = a[idx], a[i]
      permute(a, idx + 1, all_magic)
      a[idx], a[i] = a[i], a[idx]


def main():
  # read the dimension of the magic square
  in_file = open ('magic.in', 'r')
  line = in_file.readline()
  line = line.strip()
  n = int (line)
  in_file.close()

  '''
  # check if you read the input correctly
  print (n)
  '''
  # create an empty list for all magic squares
  all_magic = []

  og_list = []
  len_list = n ** 2
  # create the 1-D list that has the numbers 1 through n^2
  for i in range(len_list):
    og_list.append(i + 1)
  # generate all magic squares using permutation 
  permute(og_list, 0, all_magic)

  final_magic = []
  for i in range(len(all_magic)):
    if is_magic(all_magic[i]):
      final_magic.append(all_magic[i])
  

  # print all magic squares
  for element in final_magic:
    print(element)

if __name__ == "__main__":
  main()

