def quick_sort(arr, first=None, last=None):
    if first == None:
        first = 0
    if last == None:
        last = len(arr) - 1

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

    if last > first:

        pivot = partition(arr, first, last)
        quick_sort(arr, first, pivot-1)
        quick_sort(arr, pivot+1, last)


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

    return output # O(n) + O(nlog(n)) + O(n*k) * O(n) (( ' it was supposed to be (O(n+k) '  ))



arr = [3,3,3,3,3,3,6,2,7]
print(countingSort(arr))
print(sorted(arr) == countingSort(arr))

