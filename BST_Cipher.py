#  File: BST_Cipher.py

#  Description: Taking in a key sentence, encrypt a word and decrypt a word.

#  Date Created: 11/16/2020

#  Date Last Modified: 11/16/2020

import sys

class Node (object):
	def __init__ (self, data = None):
		self.data = data
		self.lchild = None
		self.rchild = None



class Tree (object):
	# the init() function creates the binary search tree with the
	# encryption string. If the encryption string contains any
	# character other than the characters 'a' through 'z' or the
	# space character drop that character.
	def __init__ (self, encrypt_str):
		self.root = None
		encrypt_str = encrypt_str.lower()
		#print(encrypt_str)
		for ch in encrypt_str:
			# only encrypt letters
			if (ord(ch) == 32):
				self.insert(ch.lower())
			elif ((ord(ch) >= 97 and ord(ch) <= 122)):
				self.insert(ch.lower())
			else:
				continue
		return

	# the insert() function adds a node containing a character in
	# the binary search tree. If the character already exists, it
	# does not add that character. There are no duplicate characters
	# in the binary search tree.
	def insert (self, ch):
		newNode = Node(ch)
		if (self.root == None):
			self.root = newNode
		else:
			current = self.root
			parent = self.root
			while (current != None):
				parent = current
				if (ch == current.data):
					break
				elif (ch < current.data):
					current = current.lchild
				else:
					current = current.rchild
			if (ch < parent.data):
				parent.lchild = newNode
			elif (ch > parent.data):
				parent.rchild = newNode

	# the search() function will search for a character in the binary
	# search tree and return a string containing a series of lefts
	# (<) and rights (>) needed to reach that character. It will
	# return a blank string if the character does not exist in the tree.
	# It will return * if the character is the root of the tree.
	def search (self, ch):
		if (self.root.data == ch):
			return '*'
		current = self.root
		st = ''
		while (current != None):
			if (ch == current.data):
				return st
			elif (ch < current.data):
				st += '<'
				current = current.lchild
			elif (ch > current.data):
				st += '>'
				current = current.rchild
		return st

	# the traverse() function will take string composed of a series of
	# lefts (<) and rights (>) and return the corresponding 
	# character in the binary search tree. It will return an empty string
	# if the input parameter does not lead to a valid character in the tree.
	def traverse (self, st):
		current = self.root
		for token in st:
			if (current != None):
				if (token == '*'):
					return current.data
				elif (token == '<'):
					current = current.lchild
				elif (token == '>'):
					current = current.rchild
			else:
				return ''
		return current.data

	# the encrypt() function will take a string as input parameter, convert
	# it to lower case, and return the encrypted string. It will ignore
	# all digits, punctuation marks, and special characters.
	def encrypt (self, st):
		st = st.lower()
		encrypted_string = ''
		for ch in st:
			if ((ord(ch) == 32) or ((ord(ch) >= 97) and (ord(ch) <= 122))):
				path = self.search(ch)
				if path:
					encrypted_string += path + '!'
		return encrypted_string[:-1]

	# the decrypt() function will take a string as input parameter, and
	# return the decrypted string.
	def decrypt (self, st):
		decrypted_string = ''
		st = st.lower()
		paths = st.split('!')
		for path in paths:
			decrypted_string += self.traverse(path)
		return decrypted_string


def main():
	# read encrypt string
	line = sys.stdin.readline()
	encrypt_str = line.strip()

	# create a Tree object
	the_tree = Tree (encrypt_str)

	# read string to be encrypted
	line = sys.stdin.readline()
	str_to_encode = line.strip()

	# print the encryption
	print (the_tree.encrypt(str_to_encode))

	# read the string to be decrypted
	line = sys.stdin.readline()
	str_to_decode = line.strip()

	# print the decryption
	print (the_tree.decrypt(str_to_decode))


if __name__ == "__main__":
	main()
