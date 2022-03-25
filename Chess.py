
#  File: Chess.py

#  Description: Takes in an integer n and prints the total number of ways
# that the queens can be places on the board.

#  Date Created: 10/22/2020

#  Date Last Modified: 10/23/2020

import sys

class Queens (object):
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)
    self.num_solutions = 0


  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print ()

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
    
  # do the recursive backtracking
  def recursive_solve (self, col):
    if (col == self.n):
      self.num_solutions += 1
    else:
      for i in range (self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          self.recursive_solve(col + 1)
          self.board[i][col] = '*'


  # if the problem has a solution print the board
  def solve (self):
    self.recursive_solve(0)
    print(self.num_solutions)


def main():
  # read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create a chess board
  game = Queens (n)

  # place the queens on the board and count the solutions
  game.solve()
  # print the number of solutions
 
if __name__ == "__main__":
  main()

