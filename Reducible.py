#  File: Reducible.py

#  Description: Given a file with words, program determines the
# words that reduce from 10 letters to 1, with each step being a
# word in the dictionary.

#  Student Name: Samuel Pomajevich

#  Student UT EID: SRP2938

#  Partner Name: Natania Christopher

#  Partner UT EID: nnc476

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/29/2020

#  Date Last Modified: 10/30/2020


# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
  hash_idx = hash_word(s, const)
  stepSize = const - ( hash_idx % const )
  return stepSize

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  position = hash_word(s, len(hash_table))

  if (hash_table[position] != " "):
    newPos = step_size(s, 13)

    i = 1
    while (hash_table[(position + newPos * i) % len(hash_table)] != " "):
      i += 1

    hash_table[(position + newPos * i) % len(hash_table)] = s

  else:
    hash_table[position] = s

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
  position = hash_word(s, len(hash_table))
  
  if (hash_table[position] == s):
    return True
  
  if (hash_table[position] != " "):
    newPos = step_size(s, 13)
    i = 1
    while (hash_table[(position + newPos * i) % len(hash_table)] != " "):
      if (hash_table[(position + newPos * i) % len(hash_table)] == s):
        return True
      i += 1
  return False

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  if find_word(s, hash_memo):
    return True

  # If word reduces to three given letters.
  if len(s) == 1:
    return s == "a" or s == "i" or s == "o"
  
  # Use helper function to go through all possibilities of words.
  for word in helper(s, hash_table):
    if is_reducible(word, hash_table, hash_memo):
      insert_word(s, hash_memo)
      return True
  return False


# Helper funtion to go through reducible word possibilities. 
def helper(s, hash_table):
  reducible = []
  for i in range(len(s)):
    word = s[:i] + s[i+1:]
    if find_word(word, hash_table):
      reducible.append(word)
  return reducible


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
  longestWords = []
  for word in string_list:
    if len(word) == 10:
      longestWords.append(word)
  return longestWords

def main():
  # create an empty word_list
  word_list = []

  # open the file words.txt
  with open("words.txt") as f:
    # read words from words.txt and append to word_list
      for word in f:
        line = word.strip()
        word_list.append(line)
      word_list.append("a")
      word_list.append("i")
      word_list.append("o")

  # close file words.txt
  f.close()
  
  # find length of word_list
  length_word_list = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  prime = False
  count = 0
  while prime == False:
    if is_prime(2 * length_word_list + count) == True:
      N = (2 * length_word_list + count)
      prime = True
    count += 1

  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  for i in range(N):
    hash_list.append(" ")

  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for word in word_list:
    insert_word(word, hash_list)

  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  hash_memo = []
  
  prime = False
  count = 0
  while prime == False:
    if is_prime(0.2 * length_word_list + count) == True:
      M = int((0.2 * length_word_list + count))
      prime = True
    count += 1
  
  # populate the hash_memo with M blank strings
  for i in range(M):
    hash_memo.append(" ")

  # create an empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  for word in word_list:
    if is_reducible(word, hash_list, hash_memo):
      reducible_words.append(word)
  reducible_words.sort(reverse = True)
  
  # find words of length 10 in reducible_words
  len10words = get_longest_words(reducible_words)

  # print the words of length 10 in alphabetical order
  # one word per line
  len10words.sort()
  for word in len10words:
    print(word)

if __name__ == "__main__":
  main()