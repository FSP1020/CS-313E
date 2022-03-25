
#  File: Hull.py

#  Description: Print the vertices of the convex hull starting
#  at the extreme left point and going clockwise around the convex hull

#  Student Name: Samuel Pomajevich

#  Student UT EID: SRP2938

#  Partner Name: Natania Christopher

#  Partner UT EID: nnc476

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/29/2020

#  Date Last Modified: 10/29/2020


# Input: A set of point objects in the x-y plane.

# Output: A list of point objects that define the vertices of the convex
#         hull in clockwise order.

# 1.  Sort the points by x-coordinates resulting in a sorted sequence
#     p_1 ... p_n.

# 2.  Create an empty list upper_hull that will store the vertices
#     in the upper hull.

# 3.  Append the first two points p_1 and p_2 in order into the upper_hull.

# 4.  For i going from 3 to n 

# 5.    Append p_i to upper_hull.

# 6.    While upper_hull contains three or more points and the last three
#       points in upper_hull do not make a right turn do

# 7.      Delete the middle of the last three points from upper_hull

# 8.  Create an empty list lower_hull that will store the vertices
#     in the lower hull.

# 9.  Append the last two points p_n and p_n-1 in order into lower_hull with
#     p_n as the first point.

# 10. For i going from n - 2 downto 1

# 11.   Append p_i to lower_hull

# 12.   While lower_hull contains three or more points and the last three
#       points in the lower_hull do not make a right turn do

# 13.     Delete the middle of the last three points from lower_hull

# 14. Remove the first and last points for lower_hull to avoid duplication
#     with points in the upper hull.

# 15. Append lower_hull to upper_hull and call it the convex_hull

# 16. Return the convex_hull.

import sys
import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

  def __repr__ (self):
    return str(self)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
	matrix = [[1, p.x, p.y], [1, q.x, q.y], [1, r.x, r.y]]
	det = 1 * (q.x * r.y - r.x * q.y) - (p.x) * (1 * r.y - 1 * q.y) + p.y * (1 * r.x - 1 * q.x)
	return det

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
	upper_hull = []
	upper_hull.append(sorted_points[0])
	upper_hull.append(sorted_points[1])
	for i in range(2, len(sorted_points)):
		upper_hull.append(sorted_points[i])
		while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-2], sorted_points[i]) >= 0:
			upper_hull.pop(-2)
	reversed_points = list(reversed(sorted_points))
	lower_hull = []
	lower_hull.append(reversed_points[0])
	lower_hull.append(reversed_points[1])
	for j in range(2, len(reversed_points)):
		lower_hull.append(reversed_points[j])
		while len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-2], reversed_points[j]) >= 0:
			lower_hull.pop(-2)
	lower_hull.pop(0)
	lower_hull.pop(-1)
	convex_hull = upper_hull + lower_hull
	return convex_hull



# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
	det = 0
	for i in range(len(convex_poly)):
		if i == len(convex_poly) - 1:
			det += convex_poly[i].x * convex_poly[0].y
		else:
			det += convex_poly[i].x * convex_poly[i + 1].y
	for j in range(len(convex_poly)):
		if j == len(convex_poly) - 1:
			det -= convex_poly[j].y * convex_poly[0].x
		else:
			det -= convex_poly[j].y * convex_poly[j + 1].x
	return 0.5 * abs(det)

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
  # create an empty list of Point objects
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)
  #print(sorted_points)
  # get the convex hull
  convexed_hull = convex_hull(sorted_points)
  # run your test cases

  # print your results to standard output

  # print the convex hull
  print('Convex Hull')
  for point in convexed_hull:
  	print(point)
  print()
  # get the area of the convex hull
  area = area_poly(convexed_hull)
  # print the area of the convex hull
  print('Area of Convex Hull =', area)
if __name__ == "__main__":
  main()