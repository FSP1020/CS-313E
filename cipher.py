import math
import random

# Create a table of dimensions K composed of zeros.
def create_table(P, encode):
    length = len(P)
    num_A = 0
    # Find if asterisks are needed.
    while math.sqrt(length) % 1 != 0:
        length += 1
        num_A += 1
        if encode:
            P += '*'
    # K is the dimension of square.
    K = int(math.sqrt(length))
    table = []
    i = 0
    # Create grid.
    for row in range(K):
        list = []
        for col in range(K):
            list.append(0)
        table.append(list)
    return table, P, K, num_A


# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string
def encrypt(strng):
    encode = True
    table, P, K, num_A = create_table(strng, encode)
    i = 0
    for col in range(K - 1, -1, -1):
        for row in range(K):
            letter = P[i]
            table[row][col] = letter
            i += 1
    string = pull_letters_from_table(K, table)
    return string


# Pull letters from the filled in grids, to form final strings.
def pull_letters_from_table(K, table):
    string = ''
    for row in range(K):
        for col in range(K):
            if table[row][col] != '*':
                string += table[row][col]
    return string


# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt(strng):
    encode = False
    table, Q, K, num_A = create_table(strng, encode)
    i = 0
    for row in range(K):
        for col in range(K):
            if K == num_A:
                if col == 0:
                    table[row][col] = '*'
                else:
                    table[row][col] = Q[i]
                    i += 1
            # If number of asterisks is less than K.
            elif num_A < K:
                if row >= K - num_A and col == 0:
                    table[row][col] = '*'
                else:
                    table[row][col] = Q[i]
                    i += 1
            # If number of asterisks is greater than K.
            else:
                if col == 0 or (col == 1 and row >= K - (num_A - K)):
                    table[row][col] = '*'
                else:
                    table[row][col] = Q[i]
                    i += 1
    # Reorganize table 90 degrees.
    table_new = []
    for col in range(K - 1, -1, -1):
        list = []
        for row in range(K):
            list.append(table[row][col])
        table_new.append(list)
    string = pull_letters_from_table(K, table_new)
    return string
    

def main():
  # read the strings P and Q from standard input
  P = 'IamGoingToTheStoreToBuyCandy'
  Q = 'aTenInoSgadBtTmyuooGyrToCehi'
  # encrypt the string P
  encrypted_string = encrypt(P)
  # decrypt the string Q
  decrypted_string = decrypt(Q)
  # print the encrypted string of P
  print(encrypted_string)
  # and the decrypted string of Q
  print(decrypted_string)
  for i in range(1, 100):  # max is 100
        to_test = ""
        for index in range(i):
            random_int = random.randint(97, 122)  # lowercase letters
            if (random.randint(1, 2) == 1):
                random_int -= 32  # to upppercase letters
            to_test += chr(random_int)
        print("Testing -", to_test)
        assert decrypt(encrypt(to_test)) == to_test

if __name__ == "__main__":
  main()