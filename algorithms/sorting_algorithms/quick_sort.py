# The quicksort algorithm has a worst-case running time of O(n^2) on an input array
# of n numbers. Despite this slow worst-case running time, quicksort is often the best
# practical choice for sorting because it is remarkably efficient on the average: its
# expected running time is O(nlog(n)), and the constant factors hidden in the O(nlog(n))
# notation are quite small.

import random

def partition(arr, first, last):
    if last > first:
        pivot = random.randint(first, last)
        # randomly choose pivot to ensure O(nlog(n))

        pivot_val = arr[pivot]
        # put pivot in the first index and compare the rest with it:
        arr[first], arr[pivot] = arr[pivot], arr[first]

        border = first
        for idx in range(first, last+1):
            if arr[idx] < pivot_val:
                border += 1
                arr[idx], arr[border] = arr[border], arr[idx]

        arr[first], arr[border] = arr[border], arr[first]

        return border


def quick_sort(arr, first=None, last=None):
    if first == None:
        first = 0
    if last == None:
        last = len(arr) - 1


    if last > first:

        pivot = partition(arr, first, last)
        quick_sort(arr, first, pivot-1)
        quick_sort(arr, pivot+1, last)

    return arr
################
# test
arr = [17, 41, 5, 22, 54, 6, 29, 3, 13]
quick_sort(arr, 0, 8)
print(arr)

