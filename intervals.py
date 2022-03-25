# Enter your code here. Read input from STDIN. Print output to STDOUT. Do not change predefined function names or parameters


def create_list():
    num_intervals = int(input())
    tuples_list = []
    for line in range(num_intervals):
        interval = input()
        interval = tuple(interval.split(' '))
        int_tuple1 = int(interval[0])
        int_tuple2 = int(interval[1])
        int_tuple = (int_tuple1, int_tuple2)
        tuples_list.append(int_tuple)
    return tuples_list


# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples(tuples_list):
    # Sort the list of tuples by lower bound.
    tuples_list = sorted(tuples_list)
    merged_tuples = []
    # Go through each tuple in the list.
    for high in tuples_list:
        # Check if list is empty, give it initial value to start with.        
        if not merged_tuples:
            merged_tuples.append(high)
        # If the list already contains an element, begin merging.
        else:
            low = merged_tuples[-1]
            if high[0] <= low[1]:
                upper_bound = max(low[1], high[1])
                merged_tuples[-1] = (low[0], upper_bound)
            else:
                merged_tuples.append(high)
    return merged_tuples 
    

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size(tuples_list):
    max_size = abs(tuples_list[0][1] - tuples_list[0][0])
    min_size = 0
    increasing_list = []
    while tuples_list:
        minimum = abs(tuples_list[0][1] - tuples_list[0][0])
        minimum_val = tuples_list[0]
        for i in range(len(tuples_list)):
            if abs(tuples_list[i][1] - tuples_list[i][0]) < minimum:
                minimum_val = tuples_list[i]
                minimum = abs(tuples_list[i][1] - tuples_list[i][0])
        increasing_list.append(minimum_val)
        tuples_list.remove(minimum_val)
    return increasing_list


def main():
  # open file intervals.in and read the data and create a list of tuples
  tuples_list = create_list()
  # merge the list of tuples
  merged_tuples = merge_tuples(tuples_list)
  # print the merged list
  print(merged_tuples)
  # sort the list of tuples according to the size of the interval
  increasing_tuples = sort_by_interval_size(merged_tuples)
  # print the sorted list
  print(increasing_tuples)


if __name__ == "__main__":
  main()