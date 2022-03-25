import math

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = x
    self.y = y
    self.z = z

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    distance =  math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
    self.distance = distance
    return distance

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    if self.distance == other.distance and is_equal(self.distance, other.distance):
      return True
    return False



class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    r = radius
    self.x = x
    self.y = y
    self.z = z
    self.r = r

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return  'Center: (' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + '), Radius: ' +  str(self.r)

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    area = 4 * math.pi * (self.r)**2
    return area
  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    volume = (4 / 3) * math.pi * (self.r)**3
    return volume

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    if ( p.x - self.x )**2 + (p.y - self.y)**2 + (p.z - self.z)**2 < (self.r)**2:
      return True
    return False

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    if self.x + self.r > other.x + other.r and self.x - self.r < other.x - other.r and self.y + self.r > other.y + other.r and self.y - self.r < other.y - other.r and self.z + self.r > other.z + other.r and self.z - self.r < other.z - other.r:
      return True
    return False

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    if self.x + self.r > a_cube.x + a_cube.half_diagonal and self.x - self.r < a_cube.x - a_cube.half_diagonal and self.y + self.r > a_cube.y + a_cube.half_diagonal and self.y - self.r < a_cube.y - a_cube.half_diagonal and self.z + self.r > a_cube.z + a_cube.half_diagonal and self.z - self.r < a_cube.z - a_cube.half_diagonal:
      return True
    return False

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
    if self.x + self.r > a_cyl.x + a_cyl.half_h and self.x - self.r < a_cyl.x - a_cyl.half_h and self.y + self.r > a_cyl.y + a_cyl.half_h and self.y - self.r < a_cyl.y - a_cyl.half_h and self.z + self.r > a_cyl.z + a_cyl.half_h and self.z - self.r < a_cyl.z - a_cyl.half_h:
      return True
    return False

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    # a = Point(self.x, self.y, self.z)
    # b = Point(other.x, other.y, other.z)
    z_difference  = abs(self.z - other.z)
    y_difference = abs(self.y - other.y)
    x_difference = abs(self.x - other.x)
    if self.x + self.r > other.x + other.r and self.x - self.r < other.x - other.r and self.y + self.r > other.y + other.r and self.y - self.r < other.y - other.r and self.z + self.r > other.z + other.r and self.z - self.r < other.z - other.r:
      return False
    if x_difference > self.r + other.r or y_difference > self.r + other.r or z_difference > self.r + other.r:
      return False
    return True

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
    # a = Point(self.x, self.y, self.z)
    # b = Point(a_cube.x, a_cube.y, a_cube.z)
    z_difference = abs(self.z - a_cube.z)
    y_difference = abs(self.y - a_cube.y)
    x_difference = abs(self.x - a_cube.x)
    if self.x + self.r > a_cube.x + a_cube.half_diagonal and self.x - self.r < a_cube.x - a_cube.half_diagonal and self.y + self.r > a_cube.y + a_cube.half_diagonal and self.y - self.r < a_cube.y - a_cube.half_diagonal and self.z + self.r > a_cube.z + a_cube.half_diagonal and self.z - self.r < a_cube.z - a_cube.half_diagonal:
      return False
    if x_difference > self.r + a_cube.half_diagonal or y_difference > self.r + a_cube.half_diagonal or z_difference > self.r + a_cube.half_diagonal:
      return False
    return True

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    diagonal_cube = (self.r) * 2
    #diameter of sphere = diagonal of cube
    side_cube = (diagonal_cube) / (math.sqrt(3))
    return Cube(side = side_cube)


class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.x = x
    self.y = y
    self.z = z
    self.side = side
    self.diagonal = math.sqrt(3) * self.side
    self.half_diagonal = self.diagonal / 2

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return  'Center: (' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + '), Side: ' + str(self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    area = 6 * (self.side)**2
    return area

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    volume = (self.side)**3
    return volume

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    if self.x + self.half_diagonal > p.x and self.x - self.half_diagonal < p.x and self.y + self.half_diagonal > p.y and self.y - self.half_diagonal < p.y and self.z + self.half_diagonal > p.z and self.z - self.half_diagonal < p.z:
      return True
    return False

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    if self.x + self.half_diagonal > a_sphere.x + a_sphere.r and self.x - self.half_diagonal < a_sphere.x - a_sphere.r and self.y + self.half_diagonal > a_sphere.y + a_sphere.r and self.y - self.half_diagonal < a_sphere.y - a_sphere.r and self.z + self.half_diagonal > a_sphere.z + a_sphere.r and self.z - self.half_diagonal < a_sphere.z - a_sphere.r:
      return True
    return False

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    if self.x + self.half_diagonal > other.x + other.half_diagonal and self.x - self.half_diagonal < other.x - other.half_diagonal and self.y + self.half_diagonal > other.y + other.half_diagonal and self.y - self.half_diagonal < other.y - other.half_diagonal and self.z + self.half_diagonal > other.z + other.half_diagonal and self.z - self.half_diagonal < other.z - other.half_diagonal:
      return True
    return False

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
    if self.x + self.half_diagonal > a_cyl.x + a_cyl.half_h and self.x - self.half_diagonal < a_cyl.x - a_cyl.half_h and self.y + self.half_diagonal > a_cyl.y + a_cyl.half_h and self.y - self.half_diagonal < a_cyl.y - a_cyl.half_h and self.z + self.half_diagonal > a_cyl.z + a_cyl.half_h and self.z - self.half_diagonal < a_cyl.z - a_cyl.half_h:
      return True
    return False

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    # a = Point(self.x, self.y, self.z)
    # b = Point(other.x, other.y, other.z)
    z_difference  = abs(self.z - other.z)
    y_difference = abs(self.y - other.y)
    x_difference = abs(self.x - other.x)
    if self.x + self.side / 2 > other.x + other.side / 2 and self.x - self.side / 2 < other.x - other.side / 2 and self.y + self.side / 2 > other.y + other.side / 2 and self.y - self.side / 2 < other.y - other.side / 2 and self.z + self.side / 2 > other.z + other.side / 2 and self.z - self.side / 2 < other.z - other.side / 2:
      return False
    if x_difference > (self.side + other.side) / 2 or y_difference > (self.side + other.side) / 2 or z_difference > (self.side + other.side) / 2:
      return False
    return True

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    # a = Point(self.x, self.y, self.z)
    # b = Point(other.x, other.y, other.z)
    z_difference  = abs(self.z - other.z)
    y_difference = abs(self.y - other.y)
    x_difference = abs(self.x - other.x)
    if self.x + self.side / 2 > other.x + other.side / 2 and self.x - self.side / 2 < other.x - other.side / 2 and self.y + self.side / 2 > other.y + other.side / 2 and self.y - self.side / 2 < other.y - other.side / 2 and self.z + self.side / 2 > other.z + other.side / 2 and self.z - self.side / 2 < other.z - other.side / 2:
      return 0
    if x_difference <= (self.side + other.side) / 2 or y_difference <= (self.side + other.side) / 2 or z_difference <= (self.side + other.side) / 2:
      length = abs((self.x + self.side / 2) - (other.x - other.side / 2))
      width = abs((self.y + self.side / 2) - (other.y - other.side / 2))
      height = abs((self.z + self.side / 2) - (other.z - other.side / 2))
      return length * width * height
    return 0

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    diag = self.side * math.sqrt(3)
    r = diag / 2
    sphere_c = Sphere(radius = r)
    return sphere_c

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    r = radius
    h = height
    self.x = x
    self.y = y
    self.z = z
    self.r = r
    self.h = h
    self.half_h = h / 2

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return  'Center: (' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + '), Radius: ' + str(self.r) + ', Height: ' + str(self.h)

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    area = 2 * math.pi * (self.r)**2 + 2 * math.pi * self.r * self.h
    return area

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    volume = math.pi * (self.r)**2 * self.h
    return volume

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    if self.x + self.r > p.x and self.x - self.r < p.x and self.y + self.r > p.y and self.y - self.r < p.y and self.z + self.half_h > p.z and self.z - self.half_h < p.z:
      return True
    return False

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    if self.x + self.r > a_sphere.x + a_sphere.r and self.x - self.r < a_sphere.x - a_sphere.r and self.y + self.r > a_sphere.y + a_sphere.r and self.y - self.r < a_sphere.y - a_sphere.r and self.z + self.half_h > a_sphere.z + a_sphere.r and self.z - self.half_h < a_sphere.z - a_sphere.r:
      return True
    return False

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    if self.x + self.r > a_cube.x + a_cube.half_diagonal and self.x - self.r < a_cube.x - a_cube.half_diagonal and self.y + self.r > a_cube.y + a_cube.half_diagonal and self.y - self.r < a_cube.y - a_cube.half_diagonal and self.z + self.half_h > a_cube.z + a_cube.half_diagonal and self.z - self.half_h < a_cube.z - a_cube.half_diagonal:
      return True
    return False

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    if self.x + self.r > other.x + other.r and self.x - self.r < other.x - other.r and self.y + self.r > other.y + other.r and self.y - self.r < other.y - other.r and self.z + self.half_h > other.z + other.half_h and self.z - self.half_h < other.z - other.half_h:
      return True
    return False

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
    # a = Point(self.x, self.y, self.z)
    # b = Point(other.x, other.y, other.z)
    z_difference  = abs(self.z - other.z)
    y_difference = abs(self.y - other.y)
    x_difference = abs(self.x - other.x)
    if self.x + self.r > other.x + other.r and self.x - self.r < other.x - other.r and self.y + self.r > other.y + other.r and self.y - self.r < other.y - other.r and self.z + self.half_h > other.z + other.half_h and self.z - self.half_h < other.z - other.half_h:
      return False
    if x_difference > self.r + other.r or y_difference > self.r + other.r or z_difference > self.half_h + other.half_h:
      return False
    return True

def is_equal(a, b):
  tol = 1.0e-6
  return (abs(a - b) < tol)


def main():
  # read data from standard input
  
  # read the coordinates of the first Point p
  coordinates_p = input().split()
  px = eval(coordinates_p[0])
  py = eval(coordinates_p[1])
  pz = eval(coordinates_p[2])
  # create a Point object 
  point_p = Point(px, py, pz)
  # read the coordinates of the second Point q
  coordinates_q = input().split()
  qx = eval(coordinates_q[0])
  qy = eval(coordinates_q[1])
  qz = eval(coordinates_q[2])
  # create a Point object 
  point_q = Point(qx, qy, qz)
  # read the coordinates of the center and radius of sphereA
  coordinates_sphere_a = input().split()
  s_center_x_a = eval(coordinates_sphere_a[0])
  s_center_y_a = eval(coordinates_sphere_a[1])
  s_center_z_a = eval(coordinates_sphere_a[2])
  s_r_a = eval(coordinates_sphere_a[3])
  # create a Sphere object 
  sphere_a = Sphere(s_center_x_a, s_center_y_a, s_center_z_a, s_r_a)
  # read the coordinates of the center and radius of sphereB
  coordinates_sphere_b = input().split()
  s_center_x_b = eval(coordinates_sphere_b[0])
  s_center_y_b = eval(coordinates_sphere_b[1])
  s_center_z_b = eval(coordinates_sphere_b[2])
  s_r_b = eval(coordinates_sphere_b[3])
  # create a Sphere object
  sphere_b = Sphere(s_center_x_b, s_center_y_b, s_center_z_b, s_r_b)
  # read the coordinates of the center and side of cubeA
  coordinates_cube_a = input().split()
  c_center_x_a = eval(coordinates_cube_a[0])
  c_center_y_a = eval(coordinates_cube_a[1])
  c_center_z_a = eval(coordinates_cube_a[2])
  c_r_a = eval(coordinates_cube_a[3])
  # create a Cube object 
  cube_a = Cube(c_center_x_a, c_center_y_a, c_center_z_a, c_r_a)
  # read the coordinates of the center and side of cubeB
  coordinates_cube_b = input().split()
  c_center_x_b = eval(coordinates_cube_b[0])
  c_center_y_b = eval(coordinates_cube_b[1])
  c_center_z_b = eval(coordinates_cube_b[2])
  c_r_b = eval(coordinates_cube_b[3])
  # create a Cube object 
  cube_b = Cube(c_center_x_b, c_center_y_b, c_center_z_b, c_r_b)
  #print(cube_b)
  # read the coordinates of the center, radius and height of cylA
  coordinates_cyl_a = input().split()
  cyl_center_x_a = eval(coordinates_cyl_a[0])
  cyl_center_y_a = eval(coordinates_cyl_a[1])
  cyl_center_z_a = eval(coordinates_cyl_a[2])
  cyl_r_a = eval(coordinates_cyl_a[3])
  cyl_h_a = eval(coordinates_cyl_a[4])
  # create a Cylinder object 
  cyl_a = Cylinder(cyl_center_x_a, cyl_center_y_a, cyl_center_z_a, cyl_r_a, cyl_h_a)
  #print(cyl_a)
  # read the coordinates of the center, radius and height of cylB
  coordinates_cyl_b = input().split()
  cyl_center_x_b = eval(coordinates_cyl_b[0])
  cyl_center_y_b = eval(coordinates_cyl_b[1])
  cyl_center_z_b= eval(coordinates_cyl_b[2])
  cyl_r_b = eval(coordinates_cyl_b[3])
  cyl_h_b = eval(coordinates_cyl_b[4])
  # create a Cylinder object
  cyl_b = Cylinder(cyl_center_x_b, cyl_center_y_b, cyl_center_z_b, cyl_r_b, cyl_h_b)
  #print(cyl_b)
  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
  origin = Point(0, 0, 0)
  if point_p.distance(origin) > point_q.distance(origin):
    print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
  else:
    print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')
  print()
  # print if Point p is inside sphereA
  if sphere_a.is_inside_point(point_p):
    print('Point p is inside sphereA')
  else:
    print('Point p is not inside sphereA')
  # print if sphereB is inside sphereA
  if sphere_a.is_inside_sphere(sphere_b):
    print('sphereB is inside sphereA')
  else:
    print('sphereB is not inside sphereA')
  # print if cubeA is inside sphereA
  if sphere_a.is_inside_cube(cube_a):
    print('cubeA is inside sphereA')
  else:
    print('cubeA is not inside sphereA')
  # print if cylA is inside sphereA
  if sphere_a.is_inside_cyl(cyl_a):
    print('cylA is inside sphereA')
  else:
    print('cylA is not inside sphereA')
  # print if sphereA intersects with sphereB
  if sphere_b.does_intersect_sphere(sphere_a):
    print('sphereA does intersect sphereB')
  else:
    print('sphereA does not intersect sphereB')
  # print if cubeB intersects with sphereB
  if sphere_b.does_intersect_cube(cube_b):
    print('cubeB does intersect sphereB')
  else:
    print('cubeB does not intersect sphereB')
  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
  cube_c = sphere_a.circumscribe_cube()
  if cube_c.volume() > cyl_a.volume():
    print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
  else:
    print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')
  print()
  # print if Point p is inside cubeA
  if cube_a.is_inside_point(point_p):
    print('Point p is inside cubeA')
  else:
    print('Point p is not inside cubeA')
  # print if sphereA is inside cubeA
  if cube_a.is_inside_sphere(sphere_a):
    print('sphereA is inside cubeA')
  else:
    print('sphereA is not inside cubeA')
  # print if cubeB is inside cubeA
  if cube_a.is_inside_cube(cube_b):
    print('cubeB is inside cubeA')
  else:
    print('cubeB is not inside cubeA')
  # print if cylA is inside cubeA
  if cube_a.is_inside_cylinder(cyl_a):
    print('cylA is inside cubeA')
  else:
    print('cylA is not inside cubeA')
  # print if cubeA intersects with cubeB
  if cube_a.does_intersect_cube(cube_b):
    print('cubeA does intersect cubeB')
  else:
    print('cubeA does not intersect cubeB')
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  if cube_a.intersection_volume(cube_b) > sphere_a.volume():
    print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
  else:
    print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')
  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
  sphere_c = cube_a.inscribe_sphere()
  if sphere_c.area() > cyl_a.area():
    print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
  else:
    print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')
  print()
  # print if Point p is inside cylA
  if cyl_a.is_inside_point(point_p):
    print('Point p is inside cylA')
  else:
    print('Point p is not inside cylA')
  # print if sphereA is inside cylA
  if cyl_a.is_inside_sphere(sphere_a):
    print('sphereA is inside cylA')
  else:
    print('sphereA is not inside cylA')
  # print if cubeA is inside cylA
  if cyl_a.is_inside_cube(cube_a):
    print('cubeA is inside cylA')
  else:
    print('cubeA is not inside cylA')
  # print if cylB is inside cylA
  if cyl_a.is_inside_cylinder(cyl_b):
    print('cylB is inside cylA')
  else:
    print('cylB is not inside cylA')
  # print if cylB intersects with cylA
  if cyl_a.does_intersect_cylinder(cyl_b):
    print('cylB does intersect cylA')
  else:
    print('cylB does not intersect cylA')




if __name__ == "__main__":
  main()