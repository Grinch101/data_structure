def timeit(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        print('ended in', end - start)
        return output

    return wrapper


# @timeit
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


def flatten(arr):
    def list_checker(x): return type(x) is list

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


class INT(int):

    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(str(self.data))


@timeit
def radix_sort(arr):
    d_size = max(set([len(INT(i)) for i in arr]))

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
## test:

arr = [802,12,0,1, 23, 404, 55, 67, 88, 980]
arr = radix_sort(arr)
print(sorted(arr) == arr)
print(arr)