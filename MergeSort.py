## Book Version ##

import sys


class MergeSort:

    def __init__(self, arr):
        self.merge_sort(arr)

    def merge_sort(self, arr):
        self._merge_sort(arr, 0, len(arr)-1)
        print(arr)

    def _merge_sort(self, arr, first, last):
        if first < last:
            middle = (first + last)//2
            self._merge_sort(arr, first, middle)
            self._merge_sort(arr, middle+1, last)
            self._merge(arr, first, middle, last)

    def _merge(self, arr, first, middle, last):
        L = arr[first:middle+1]
        R = arr[middle+1:last+1]
        L.append(sys.maxsize)
        R.append(sys.maxsize)
        i = j = 0

        for k in range(first, last+1):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1


### TEST ###
arr = [5, 9, 1, 2, 4, 8, 6, 3, 7]

mg = MergeSort(arr)
