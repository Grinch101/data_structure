# Bucket sort assumes that the input is drawn from a uniform distribution and has an
# average-case running time of O(n). Like counting sort, bucket sort is fast because
# it assumes something about the input.

# Bucket sort divides the interval [0,1) into n equal-sized subintervals, or buckets,
# and then distributes the n input numbers into the buckets. Since the inputs are uniformly
# and independently distributed over [0,1), we do not expect many numbers
# to fall into each bucket. To produce the output, we simply sort the numbers in each
# bucket and then go through the buckets in order, listing the elements in each.

# from data_structures.LinkedList import LinkedList
from quick_sort import quick_sort
from  data_structures import LinkedList

def bucket_sort(arr, max_num, standardized = False):
    if not standardized:
        for i in range(len(arr)):
            arr[i] = arr[i] / (max_num)  # standardize
    else:
        max_num = 1
    ## create 10 buckets:
    buckets = [LinkedList.LinkedList() for i in range(0, 10)]
    # print(buckets)
    # determine each item's bucket and assign it to that:
    i = 0
    while i < len(arr):  # adding each item to its bucket
        n = int(arr[i] * 10)
        linked_list = buckets[n]
        linked_list.add_left(arr[i])
        i += 1

    sorted_vals = []
    for linked_list in buckets:
        vals = [item.data for item in linked_list]
        quick_sort(vals)
        sorted_vals = sorted_vals + vals
    for i in range(len(sorted_vals)):
        sorted_vals[i] = ((sorted_vals[i]) * (max_num))
    return sorted_vals
    