
#  File: Boxes.py

#  Description: Program determines how many boxes fit within other boxes.

#  Date Created: 10/14/2020

#  Date Last Modified: 10/16/2020

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
  hi = len(box_list)
  if (idx == hi):
      all_box_subsets.append(sub_set) 
      return
  else:
      c = sub_set[:]
      sub_set.append(box_list[idx])
      sub_sets_boxes(box_list, c, idx + 1, all_box_subsets)
      if len(sub_set) > 1:
          # Check if boxes fit in other boxes.
          if does_fit(sub_set[len(sub_set) - 2], sub_set[len(sub_set) - 1]):
              sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
      else:
          sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
  return

# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets(all_box_subsets, largest_size, all_nesting_boxes):
  largest_size = 0
  for subset in all_box_subsets:
    if len(subset) > largest_size:
      largest_size = len(subset)
  if largest_size < 2:
    return 1
  return largest_size

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  in_file = open ('boxes.in', 'r')
  line = in_file.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # close the file
  in_file.close()

  '''
  # print to make sure that the input was read in correctly
  print (box_list)
  print()
  '''

  # sort the box list
  box_list.sort()

  '''
  # print the box_list to see if it has been sorted.
  print (box_list)
  print()
  '''

  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)

  subs = []

  max_nest_length = 1
  for entry in all_box_subsets:
      if len(entry) > max_nest_length:
          max_nest_length = len(entry)
      
  # Print largest set of nesting boxes
  if max_nest_length >= 2:
      for entry in all_box_subsets:
          boxes = []
          if len(entry) == max_nest_length:
              for box in entry:
                  boxes.append(box)
              subs.append(boxes)

  all_box_subsets = subs

  # initialize the size of the largest sub-set of nesting boxes
  largest_size = 0

  # create a list to hold the largest subsets of nesting boxes
  all_nesting_boxes = []

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  largest_subset = largest_nesting_subsets(all_box_subsets, largest_size, all_nesting_boxes)

  # print the largest number of boxes that fit
  print(largest_subset)
  # print the number of sets of such boxes
  number_of_sets = len(all_box_subsets)

  if number_of_sets != 0:
    print(number_of_sets)
  else:
    print(len(box_list))

if __name__ == "__main__":
  main()

