# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
  width = rect[2] - rect[0]
  height = rect[3] - rect[1]
  return width * height  


def fill_grid(rows, columns):
  zero_grid = []
  for i in range(rows):
    row = []
    for j in range(columns):
      row.append(0)
    zero_grid.append(row)
  return zero_grid


def unallocated(grid, rect):
  for x in range(len(grid)):
    for y in range(len(grid[0])):
      if rect[0] <= x < rect[2] and rect[1] <= y < rect[3]:
        grid[x][y] = 1
  unallocated = 0
  for x in range(len(grid)):
    for y in range(len(grid[0])):
      if grid[x][y] == 0:
        unallocated += 1
  return unallocated


def employee_grid(grid, rect):
  grid = fill_grid(len(grid), len(grid[0]))
  for x in range(len(grid)):
    for y in range(len(grid[0])):
      if rect[0] <= x < rect[2] and rect[1] <= y < rect[3]:
        grid[x][y] = 1
  return grid

def contested_grid(grid1, rect):
  overlap = 0
  for x in range(len(grid1)):
    for y in range(len(grid1[0])):
      if rect[0] <= x < rect[2] and rect[1] <= y < rect[3]:
        if grid1[x][y] == 1:
          overlap += 1
  return overlap


def fresh_grid(list_of_grids):
  new_list_grids = []
  for i in range(len(list_of_grids)):
    grid0 = fill_grid(len(list_of_grids[i]), len(list_of_grids[i][0]))
    for j in range(len(list_of_grids)):
      if i != j:
        for x in range(len(list_of_grids[i])):
          for y in range(len(list_of_grids[i][x])):
            if list_of_grids[j][x][y] != 0:
              grid0[x][y] = 1
    new_list_grids.append(grid0)
  return new_list_grids

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases

  return "all test cases passed"


def input_employee_info():
  num_employees = int(input())
  dictionary_of_employees = {}
  list_of_employees = []
  list_of_coords = []
  for i in range(num_employees):
    name_and_coords = input().split()
    name = name_and_coords[0]
    for j in range(1, 5):
      name_and_coords[j] = int(name_and_coords[j])
    coords = tuple(name_and_coords[1:])
    list_of_coords.append(coords)
    dictionary_of_employees[name] = coords
    list_of_employees.append(name)
  return dictionary_of_employees, list_of_employees, \
    num_employees, list_of_coords


def main():
  # read the data
  w_h = input().split()
  rows = int(w_h[0])
  columns = int(w_h[1])
  bldg = (0, 0, rows, columns)

  # compute the total office space
  print('Total', area(bldg))
  zero_grid = fill_grid(rows, columns)
  dictionary_of_employees, list_of_employees, num_employees, \
    cubicles = input_employee_info()

  # compute the total unallocated space
  for h in range(len(list_of_employees)):
    unallocated_area = unallocated(zero_grid, cubicles[h])
  print('Unallocated', unallocated_area)
  list_of_grids = []
  for i in range(len(list_of_employees)):
    new_grid = employee_grid(zero_grid, cubicles[i])
    list_of_grids.append(new_grid)

  # compute the total contested space
  new_list_grids = fresh_grid(list_of_grids)
  contested_area = 0
  for a in range(len(list_of_employees)):
    uncontested_area = contested_grid(new_list_grids[a], cubicles[a])
    contested_area += area(cubicles[a]) - uncontested_area
  contested_area = area(bldg) - unallocated_area - contested_area
  print('Contested', contested_area)

  # compute the uncontested space that each employee gets
  for s in range(len(list_of_employees)):
    uncontested_area = contested_grid(new_list_grids[s], cubicles[s])
    print(list_of_employees[s], area(cubicles[s]) - uncontested_area)
  

if __name__ == "__main__":
  main()