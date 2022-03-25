#!/bin/python3

import os
import re
import sys
import math

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

# compute and return the determinant of the coordinates of three points
# p, q, and r are Point objects
def det (p, q, r):
    matrix = [[1, p.x, p.y], [1, q.x, q.y], [1, r.x, r.y]]
    det = 1 * (q.x * r.y - r.x * q.y) - (p.x) * (1 * r.y - 1 * q.y) + p.y * (1 * r.x - 1 * q.x)
    return det
# computes and returns the convex hull of a sorted list of Points
# convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order
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

def main(coords):
    # create an empty list of Point objects
  points = []
  # read data from standard input
  num_points = len(coords)
  # read line by line, create Point objects and store in a list
  for i in range(num_points):
      point = (coords[i][0], coords[i][1])
      point = Point(int(point[0]), int(point[1]))
      points.append(point)
  # sort the list according to x-coordinates
  sorted_points = sorted(points)
  #print(sorted_points)
  # get the convex hull
  convexed_hull = convex_hull(sorted_points)
  # run your test cases

  # print your results to standard output
  return convexed_hull
  # print the convex hull
  # print('Convex Hull')
  # for point in convexed_hull:
      # print(point)
  # print()

if __name__ == "__main__":
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  inpt = sys.stdin.read().split()
  coords = []
  for i in range(1, (int(inpt[0])*2), 2):
    coords.append((int(inpt[i]), int(inpt[i+1])))
  result = main(coords)
  for point in result:
    fptr.write(str(point.x) + ' ' + str(point.y) + '\n')
  fptr.close()  