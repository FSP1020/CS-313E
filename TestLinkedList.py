# File: TestLinkedList.py

#  Description: Helper methods for the LinkedList class that we developed in 
#  class and testing them in main.

#  Date Created: 11//8/2020

#  Date Last Modified: 11/8/2020

class Link (object):
	def __init__ (self, data, next = None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)


class LinkedList (object):
    # create a linked list
    def __init__ (self):
       self.first = None

    # get number of links 
    def get_num_links (self):
    	num_links = 0
    	current = self.first
    	while current != None:
    		num_links += 1
    		current = current.next
    	return num_links

    # add an item at the beginning of the list
    def insert_first (self, data):
    	new_link = Link(data)
    	new_link.next = self.first
    	self.first = new_link

    # add an item at the end of a list
    def insert_last (self, data):
    	new_link = Link (data)
    	current = self.first
    	if (current == None):
    		self.first = new_link
    		return
    	while (current.next != None):
    		current = current.next
    	current.next = new_link

    # add an item in an ordered list in ascending order
    def insert_in_order (self, data): 
    	if self.first == None:
    		self.insert_first(data)
    		return
    	if data < self.first.data:
	        self.insert_first(data)
	        return
    	else:
	    	new_link = Link(data)
	    	current = self.first
	    	previous = self.first
	    	while (data > current.data):
	    		if current.next == None:
	    			self.insert_last(data)
	    			return
	    		else:
	    			previous = current
	    			current = current.next
	    	previous.next = new_link
	    	new_link.next = current

	# search in an unordered list, return None if not found
    def find_unordered (self, data): 
        current = self.first
        if current == None:
        	return None
        else:
        	while (current.data != data):
        		if current.next == None:
        			return None
        		else:
        			current = current.next
        	return current

	# Search in an ordered list, return None if not found
    def find_ordered (self, data): 
    	current = self.first
    	if current == None:
    		return None
    	while (current.data != data):
    		if current.next == None:
    			return None
    		else:
    			if current.next.data > data:
    				return None 
    			else:
    				current = current.next
    	return current

	# Delete and return Link from an unordered list or None if not found
    def delete_link (self, data):
    	current = self.first
    	previous = self.first
    	if (current == None):
    		return None

    	while (current.data != data):
    		if (current.next == None):
    			return None
    		else:
    			previous = current
    			current = current.next

    	if (current == self.first):
    		self.first = self.first.next
    	else:
    		previous.next = current.next

    	return current

	# String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
    	current = self.first
    	count = 0
    	string = ''    
    	if self.is_empty():
    		return 'LinkedList is Empty'
    	for i in range(self.get_num_links() - 1):
    		string += str(current.data) + '  '
    		current = current.next
    		count += 1
    		if (count) % 10 == 0:
    			string += '\n'
    	string += str(current.data)
    	return string

	# Copy the contents of a list and return new list
    def copy_list (self):
    	copied_list = LinkedList()
    	current = self.first
    	while (current != None):
    		copied_list.insert_last(current.data)
    		current = current.next
    	return copied_list

	# Reverse the contents of a list and return new list
    def reverse_list (self): 
    	reversed_list = LinkedList()
    	current = self.first
    	while (current != None):
    		reversed_list.insert_first(current.data)
    		current = current.next
    	return reversed_list

	# Sort the contents of a list in ascending order and return new list
    def sort_list (self):
    	sorted_list = LinkedList()
    	if self.is_empty():
    		return sorted_list
    	current = self.first
    	for i in range(self.get_num_links()):
    		sorted_list.insert_in_order(current.data)
    		current = current.next
    	return sorted_list

	# Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
    	current = self.first
    	if self.is_empty() or self.get_num_links() == 1:
    		return True
    	for i in range(self.get_num_links() - 1):
    		if current.data > current.next.data:
    			return False
    		current = current.next
    	return True 

	# Return True if a list is empty or False otherwise
    def is_empty (self):
    	return (self.first == None)

	# Merge two sorted lists and return new list in ascending order
    def merge_list (self, other): 
    	current = other.first
    	merged_list = self.copy_list().sort_list()

    	if self.is_empty():
    		if other.is_empty():
    			return merged_list
    		else:
    			merged_list = other.copy_list()
    			return merged_list
    	elif other.is_empty():
    		return merged_list

    	for i in range(other.get_num_links()):
    		merged_list.insert_in_order(current.data)
    		current = current.next

    	return merged_list

	# Test if two lists are equal, item by item and return True
    def is_equal (self, other):
    	if self.get_num_links() != other.get_num_links():
    		return False
    	if self.is_empty() and other.is_empty():
    		return True

    	current1 = self.first
    	current2 = other.first

    	for i in range(self.get_num_links()):
    		if current1.data != current2.data:
    			return False
    		current1 = current1.next
    		current2 = current2.next
    	return True

	# Return a new list, keeping only the first occurence of an element
	# and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
    	no_dup_list = self.copy_list()
    	previous = no_dup_list.first
    	current = no_dup_list.first
    	items = []

    	for i in range(no_dup_list.get_num_links()):
    		if current.data in items:
    			current = current.next
    			previous.next = current
    		else:
    			items.append(current.data)
    			previous = current
    			current = current.next

    	return no_dup_list


def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  print("Testing insert_first() & __str__().")
  test = LinkedList()
  for i in range (40, 0, -2):
    test.insert_first(i)
  print(test)
  print("\n")

  # Test method insert_last()
  print("Testing insert_last()().")
  test.insert_last(50)
  print(test)
  print("\n")

  # Test method insert_in_order()
  print("Testing insert_in_order().")
  test.insert_in_order(25)
  print(test)
  print("\n")

  # Test method get_num_links()
  print("Testing get_num_links().")
  print(test.get_num_links())
  print("\n")

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 
  print("Testing find_unordered().")
  for i in range(10):
  	print(test.find_unordered(i))
  print("\n")

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 
  print("Testing find_ordered().")
  print(test.find_ordered(12))
  print(test.find_ordered(45))  
  print("\n")

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 
  print("Testing delete_link().")
  print(test.delete_link(2))
  print(test.delete_link(100))
  print("\n")

  # Test method copy_list()
  print("Testing copy_list().")
  print(test.copy_list())
  print("\n")

  # Test method reverse_list()
  print("Testing reverse_list().")
  print(test.reverse_list())
  print("\n")

  # Test method sort_list()
  print("Testing sort_list().")
  print(test.sort_list())
  print("\n")

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print("Testing is_sorted().")
  print(test.sort_list().is_sorted())
  print(test.is_sorted())
  test2 = LinkedList()
  test2.insert_first(50)
  test2.insert_first(40)
  print(test2)
  print("\n")

  # Test method is_empty()
  print("Testing is_empty().")
  test3 = LinkedList()
  print(test.is_empty())
  print(test3.is_empty())
  print("\n")

  # Test method merge_list()
  print("Testing method merge_list().")
  test4 = LinkedList()
  for i in range (35, 45, 2):
    test4.insert_last(i)
  test5 = LinkedList()
  for i in range (40, 50, 2):
    test5.insert_last(i)
  merged = test4.merge_list(test5)
  print(merged)
  print("\n")

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  print("Testing is_equal().")
  print(test4.is_equal(test4))
  print(test4.is_equal(test5))
  print("\n")

  # Test remove_duplicates()
  print("Testing remove_duplicates().")
  test6 = LinkedList()
  for i in range (1, 10):
    test6.insert_last(0)
    test6.insert_last(2)
  removed = test6.remove_duplicates()
  print(removed)
  print("\n")

if __name__ == "__main__":
  main()
