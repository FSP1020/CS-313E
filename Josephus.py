#  File: Josephus.py

#  Description: Use circular linked list to determine
#  last soldier standing.

#  Date Created: 11/9/2020

#  Date Last Modified: 11/10/2020

import sys

class Link(object):
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

class CircularList(object):
  # Constructor
  def __init__ ( self ): 
  	self.first = None

  # Insert an element (value) in the list
  def insert ( self, data ):
    new_link = Link(data)
    current = self.first
    if (current == None):
        self.first = new_link
        new_link.next = self.first
        return
    while (current.next != self.first):
        current = current.next
    current.next = new_link
    new_link.next = self.first

  # Find the link with the given data (value)
  def find ( self, data ):
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  # Delete a link with a given data (value)
  def delete ( self, data ):
  	current = self.first
  	previous = self.first

  	if (current == None):
  		return None

  	while (previous.next != self.first):
  		previous = previous.next

  	while (current.data != data):
  		previous = current
  		current = current.next

  	if (self.first != self.first.next):
  		self.first = current.next
  	else:
  		self.first = None

  	previous.next = current.next

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
    if self.first == None:
        return None
    current = self.first
    while (current.data != start):
        current = current.next
    count = 1
    while (count != n):
        current = current.next
        count += 1
    self.delete(current.data)
    print(current.data)
    return current.next

  # Return a string representation of a Circular List
  def __str__ ( self ):
  	string = ""
  	current = self.first
  	while (current.next != self.first):
  		string += str(current.data) + " "
  		current = current.next
  	return string


def main():
	# read number of soldiers
	line = sys.stdin.readline()
	line = line.strip()
	num_soldiers = int (line)

	# read the starting number
	line = sys.stdin.readline()
	line = line.strip()
	start_count = int (line)

	# read the elimination number
	line = sys.stdin.readline()
	line = line.strip()
	elim_num = int (line)

	# your code
	soldiers = CircularList()

	for i in range (1, num_soldiers + 1):
		soldiers.insert(i) 

	for i in range (1, num_soldiers):
		start_count = soldiers.delete_after(start_count, elim_num)
		start_count = start_count.data

	for i in range (num_soldiers + 1, num_soldiers + 2):
		start_count = soldiers.delete_after(start_count, elim_num)
		start_count = start_count.data


if __name__ == "__main__":
  main()
