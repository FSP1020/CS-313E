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

  # get the area of the convex hull
  area = area_poly(convexed_hull)
  # print the area of the convex hull
  return area

if __name__ == "__main__":
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  inpt = sys.stdin.read().split()
  coords = []
  for i in range(1, (int(inpt[0])*2), 2):
    coords.append((int(inpt[i]), int(inpt[i+1])))
  fptr.write(str(main(coords)))
  fptr.close()  