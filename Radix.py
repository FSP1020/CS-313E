
#  File: Radix.py

#  Description: Given list of strings with nums and letters,
# use radix sorting to sort.

#  Date Created: 11/2/2020

#  Date Last Modified: 11/2/2020

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  def get_list (self):
    return self.queue

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

'''
# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  sorted_list = []
  max_digits = 0
  for item in a:
    if len(item) > max_digits:
      max_digits = len(item)
  p = []
  for item in a:
    while len(item) != max_digits:
      item += '!'
    p.append(item)
  print(p)

  dictionary = {}
  queues = []
  for i in range(36):
    queues.append([])
  for num in range(10):
    dictionary[str(num)] = num
  count = 10
  for letter in range(ord('a'), ord('z') + 1):
    dictionary[chr(letter)] = count
    count += 1
  print(dictionary)
  #print(max_digits)
  for digit in range(max_digits -1, -1, -1):
    for item in p:
      for key in dictionary:
        if item[digit] == key:
          queues[dictionary[key]].enqueue(item)
          print(queues[dictionary[key]].get_list())
    
  return sorted_list
'''

def radix_sort(a):
  max_digits = 0
  for item in a:
    if len(item) > max_digits:
      max_digits = len(item)

  p = []
  for item in a:
    while len(item) != max_digits:
      item += '!'
    p.append(item)

  #print(p)

  dictionary = {}
  queues = []
  for i in range(37):
    queues.append([])
  dictionary['!'] = 0
  for num in range(10):
    dictionary[str(num)] = num + 1
  count = 11
  for letter in range(ord('a'), ord('z') + 1):
    dictionary[chr(letter)] = count
    count += 1
  
  #print(dictionary)
  sorted_list = p

  for digit in range(max_digits):
    #print(max_digits - 1 - digit)
    #print(sorted_list)
    for item in sorted_list:
      for key in dictionary:
        if item[max_digits - 1 - digit] == key:
          queues[dictionary[key]].append(item)
    #print(queues[dictionary['0']])
    sorted_list = []
    new_list = []
    for key in dictionary:
      if not empty(queues[dictionary[key]]):
          sorted_list.append(queues[dictionary[key]])
          queues[dictionary[key]] = []
    for i in range(len(sorted_list)):
      for item in sorted_list[i]:
        new_list.append(item)
    sorted_list = new_list
  #print(sorted_list)

  sorted_list = remove_special(sorted_list)

  return sorted_list

def remove_special(ls):
  p = []
  for item in ls:
    last_ch = '!'
    counter = len(item) - 1
    while last_ch == '!':
      if item[counter] == '!':
        last_ch = '!'
        counter -= 1
      else:
        last_ch = '0'
    p.append(item[0 : counter + 1])
  return p



def empty(s):
  if len(s) == 0:
    return True
  return False


def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  '''
  # Testing...
  check_list = sorted(word_list)

  for i in range(len(sorted_list)):
    if sorted_list[i] != check_list[i]:
      fail = True
    else:
      fail = False
  if fail:
    print('Fail')
  else:
    print('Success')
  '''

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()
