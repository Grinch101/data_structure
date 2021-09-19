from utilities.decor import timeit
from utilities.datatypes import INT
from quick_sort import quick_sort


def flatten(arr):
    list_checker = lambda x : type(x) is list

    while any(list(map(list_checker, arr))):
        lst = []
        i = 0
        for i in range(0, len(arr)):
            if type(arr[i]) == list:
                _len = len(arr[i])
                for j in range(0, _len):
                    lst.append(arr[i][j])

            elif type(arr[i]) == int:
                lst.append(arr[i])

        arr = lst

    return lst  # O(n*k) k is max of _len


@timeit
def radix_sort(arr):
    d_size = [len(INT(i)) for i in arr]
    quick_sort(d_size)
    d_size = d_size[-1]

    for d in range(0, d_size):

        buckets = ['empty' for i in range(0, 10)]
        for i in range(0, 10):
            lst = [num for num in arr if (num//10**d) % 10 == i]
            quick_sort(lst)  # O(nlog(n))
            buckets[i] = lst

        # flatten = (10*k) k = similar digits number, worst k = 10
        arr = flatten(buckets)

    # Total = Sum ( O(d*n) + O(nLog(n)) + O(10*10)  ) ≈ O(n(d+log(n)))
    return arr

###################
# test:


arr = [802, 12, 0, 1, 23, 404, 55, 67, 88, 980]
arr = radix_sort(arr)
print(arr)
