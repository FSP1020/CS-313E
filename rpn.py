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

def operate(oper1, oper2, token):
  expr = str(oper1) + token + str(oper2)
  return eval(expr)



def rpn (s):
  theStack = Stack()
  operators = ['+', '-', '*', '/', '//', '%', '**']

  tokens = s.split()

  for item in tokens:
    if (item in operators):
      oper2 = theStack.pop()
      oper1 = theStack.pop()
      theStack.push (operate (oper1, oper2, item))
    else:
      theStack.push (item)

  return theStack.pop()


def main():
  line = '2 3 + 5 *'
  value = rpn (line)
  print(line, '=', value)

main()
