
# Counting sort assumes that each of the n input elements is an integer in the range
# 0 to k, for some integer k. When k D O.n/, the sort runs in ‚.n/ time.
# Counting sort determines, for each input element x, the number of elements less
# than x. It uses this information to place element x directly into its position in the
# output array. For example, if 17 elements are less than x, then x belongs in output
# position 18. We must modify this scheme slightly to handle the situation in which
# several elements have the same value, since we do not want to put them all in the
# same position.
# An important property of counting sort is that it is stable: numbers with the same
# value appear in the output array in the same order as they do in the input array. That
# is, it breaks ties between two numbers by the rule that whichever number appears
# first in the input array appears first in the output array. Normally, the property of
# stability is important only when satellite data are carried around with the element
# being sorted.

from algorithms.sorting_algorithms.quick_sort import quick_sort

##############
# we use quick sort a an stable sort:
def presence(arr, item):
    for i in range(len(arr)):
        return item == arr[i]
    return False


def _count(arr, item):
    i = 0
    for val in arr:
        if item == val:
            i+=1
    return i


def getUnique(arr):
    uniques = []
    for i in range(len(arr)):
        if presence(uniques, arr[i]):
            continue
        else:
            uniques.append(arr[i])
    return uniques


def countingSort(arr):
# in counting sort we need to know some information about the array.
# we need to know number of unique numbers in the array to have O(n+k)
    uniques = getUnique(arr) # O(n)
    quick_sort(uniques) # O(nlog(n))

    # count unique values cumulitavely
    count_hash = {  item:_count(arr,item)  for item in uniques } # O(n*k)
    output = []
    for item in uniques: # O(n)
        occurance = count_hash[item]
        i = 1
        while i <= occurance:
            output.append(item)
            i += 1

    return output # O(n) + O(nlog(n)) + O(n*k) * O(n) 


### Debug
arr = [3,3,3,3,3,3,6,2,7]
print(countingSort(arr))
print(sorted(arr) == countingSort(arr))

