#  File: TestBinaryTree.py

#  Description: Takes in three possible trees and tests whether they
#  are similar, prints a level of the tree, the height and the number of nodes.

#  Date Created: 11/19/2020

#  Date Last Modified: 11/20/2020

import sys

class Node (object):
	def __init__ (self, data):
		self.data = data
		self.lChild = None
		self.rChild = None

class Tree (object):
	def __init__ (self):
		self.root = None

	# insert data into the tree
	def insert (self, data):
		new_node = Node (data)

		if (self.root == None):
			self.root = new_node
			return
		else:
			current = self.root
			parent = self.root
			while (current != None):
				parent = current
				if (data < current.data):
				  current = current.lChild
				else:
				  current = current.rChild

			# found location now insert node
			if (data < parent.data):
				parent.lChild = new_node
			else:
				parent.rChild = new_node

	# search for a node with given data
	def find (self, data):
		current = self.root
		while (current != None) and (current.data != data):
			if (data < current.data):
				current = current.lChild
			else:
				current = current.rChild
		return current

	# find the node with the minimum key
	def find_min (self):
		current = self.root
		parent = self.root
		while (current != None):
			parent = current
			current = current.lChild
		return parent

	# find the node with the maximum key
	def find_max (self):
		current = self.root
		parent = self.root
		while (current != None):
			parent = current
			current = current.rChild
		return parent

	# in order traversal - left, center, right
	def in_order (self, aNode):
		if (aNode != None):
			self.in_order (aNode.lChild)
			print (aNode.data)
			self.in_order (aNode.rChild)

	# pre order traversal - center, left, right
	def pre_order (self, aNode):
		if (aNode != None):
			print (aNode.data)
			self.pre_order (aNode.lChild)
			self.pre_order (aNode.rChild)

	# post order traversal - left, right, center
	def post_order (self, aNode):
		if (aNode != None):
			self.post_order (aNode.lChild)
			self.post_order (aNode.rChild)
			print (aNode.data)

	# Returns true if two binary trees are similar
	def is_similar (self, pNode):
		return self.is_similar_helper (self.root, pNode)

	def is_similar_helper (self, aNode1, aNode2):
		if aNode1 == None and aNode2 == None:
			return True
		elif ( (aNode1.data == aNode2.data) and
			self.is_similar_helper(aNode1.lChild, aNode2.lChild) and
			self.is_similar_helper(aNode1.rChild, aNode2.rChild)):
			return True
		else:
			return False

	# Prints out all nodes at the given level
	def print_level (self, level): 
		if self.root == None:
			return None
		else:
			self.print_level_helper(self.root,level,1)
    
	def print_level_helper(self,r,desired,current):
		if r == None:
			return
		elif (desired == current):
			print (r.data,end=' ')
		else:
			self.print_level_helper(r.lChild,desired,current+1)
			self.print_level_helper(r.rChild,desired,current+1)

	# Returns the height of the tree
	def get_height (self): 
		if self.root == None:
			return 0
		else:
			return (self.get_height_helper(self.root))

	def get_height_helper(self, node):
		if node == None:
			return -1
		else:
			return 1 + max(self.get_height_helper(node.lChild),self.get_height_helper(node.rChild))

	# Returns the number of nodes in the left subtree and
	# the number of nodes in the right subtree and the root
	def num_nodes (self):
		if self.root == None:
			return 0
		else:
			return (self.num_nodes_helper(self.root))

	def num_nodes_helper(self,r):
		if (r == None):
			return 0
		else:
			return (self.num_nodes_helper(r.lChild)+1+self.num_nodes_helper(r.rChild))


def main():
	# Create three trees - two are the same and the third is different
	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree1_input = list (map (int, line)) 	# converts elements into ints

	tree1 = Tree ()
	for num in tree1_input:
		tree1.insert(num)

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree2_input = list (map (int, line)) 	# converts elements into ints

	tree2 = Tree ()
	for num in tree2_input:
		tree2.insert(num)

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree3_input = list (map (int, line)) 	# converts elements into ints

	tree3 = Tree ()
	for num in tree3_input:
		tree3.insert(num)


	# From Piazza student...
	print(tree1.is_similar(tree2.root))
	print(tree1.is_similar(tree3.root))
	print()
	for i in range(1,tree1.get_height()+2):
		tree1.print_level(i)
		print()
	print()
	for i in range(1,tree3.get_height()+2):
		tree3.print_level(i)
		print()
	print()
	print(tree1.get_height(), tree2.get_height(), tree3.get_height())
	print()
	print(tree1.num_nodes(), tree2.num_nodes(), tree3.num_nodes())

	print()
	print()
	print('More Tests...')
	print()

	# From Piazza TA..

	#Test is_similar for every combination of trees
	print(tree1.is_similar(tree2.root))
	print(tree1.is_similar(tree3.root))
	print()
	print(tree2.is_similar(tree1.root))
	print(tree2.is_similar(tree3.root))
	print()
	print(tree3.is_similar(tree1.root))
	print(tree3.is_similar(tree2.root))
	print()

	#Lets assume that tree1 and tree2 are different
	#print different levels
	tree1.print_level(2) #assumed to print out on one line
	print() #if you need it to ensure the print_levels are on two different lines
	tree2.print_level(2) #assumed to print out on one line
	print()

	tree1.print_level(5) #assumed to print out on one line
	print() #if you need it to ensure the print_levels are on two different lines
	tree2.print_level(5) #assumed to print out on one line
	print()

	#print heights
	print(tree1.get_height())
	print(tree2.get_height())

	#print num_nodes of each tree
	print(tree1.num_nodes())
	print(tree2.num_nodes())
	print(tree3.num_nodes())
	

if __name__ == "__main__":
  main()
