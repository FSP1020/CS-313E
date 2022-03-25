#  File: ExpressionTree.py

#  Description: Read a file expression.in and create an expression tree. 
#  The expression will be a valid infix expression with the all the necessary 
#  parentheses so that there is no ambiguity in the order of the expression. 
#  Evaluate the expression and print the result. 
#  Print the prefix and postfix versions of the same expression without any parentheses.

#  Student's Name: Samuel Pomajevich

#  Student's UT EID: SRP2938

#  Partner's Name: Natania Christopher

#  Partner's UT EID: nnc476

#  Course Name: CS 313E 

#  Unique Number: 50845

#  Date Created: 11/12/2020

#  Date Last Modified: 11/12/2020

import sys

class Stack (object):
	def __init__ (self):
		self.stack = []

	# add an item on the top of the stack
	def push (self, item):
		self.stack.append (item)

	# remove an item from the top of the stack
	def pop (self):
		return self.stack.pop()

	# check the item on the top of the stack
	def peek (self):
		return self.stack[-1]

	# check if the stack is empty
	def is_empty (self):
		return (len(self.stack) == 0)

	# return the number of elements in the stack
	def size (self):
		return (len(self.stack))


class Node (object):
	def __init__(self, data = None):
		self.data = data
		self.lChild = None
		self.rChild = None


class Tree (object):
	def __init__ (self):
		self.root = Node()

	def create_tree (self, expr):
		equation = expr.split()
		parent_node = Stack()
		current_node = self.root

		for token in equation:
			if token == '(':
				parent_node.push(current_node)
				current_node.lChild = Node()
				current_node = current_node.lChild
			elif token in ['+', '-', '*', '/', '//', '%', '**']:
				current_node.data = token
				parent_node.push(current_node)
				current_node.rChild = Node()
				current_node = current_node.rChild
			elif token.isdigit() or '.' in token:
				current_node.data = token
				current_node = parent_node.pop()
			elif token == ')':
				if not parent_node.is_empty():
					current_node = parent_node.pop()
			else:
				break

	def evaluate (self, aNode):
		if aNode.data == '+':
			return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
		elif aNode.data == '-':
			return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild) 
		elif aNode.data == '*':
			return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
		elif aNode.data == '/':
			return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
		elif aNode.data == '//':
			return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
		elif aNode.data == '%':
			return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
		elif aNode.data == '**':
			return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)
		elif aNode.data.isdigit() or '.' in aNode.data:
			return eval(aNode.data)

	def pre_order (self, aNode):
		if (aNode != None):
			print(aNode.data, end= " ")
			self.pre_order(aNode.lChild)
			self.pre_order(aNode.rChild)

	def post_order (self, aNode):
		if (aNode != None):
			self.post_order(aNode.lChild)
			self.post_order(aNode.rChild)
			print(aNode.data, end= " ")


def main():
	# read infix expression
	line = sys.stdin.readline()
	expr = line.strip()
	tree = Tree()

	# evaluate the expression and print the result
	tree = Tree()
	tree.create_tree(expr)
	print(expr, '=', float(tree.evaluate(tree.root)), "\n")

	# get the prefix version of the expression and print
	print("Prefix Expression:", end= " ")
	preFix = tree.pre_order(tree.root)
	print('\n')

	# get the postfix version of the expression and print
	print("Postfix Expression:", end= " ")
	postFix = tree.post_order(tree.root)


if __name__ == "__main__":
  main()