def quick_sort(arr, first, last):

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


################
# test
arr = [17, 41, 5, 22, 54, 6, 29, 3, 13]
quick_sort(arr, 0, 8)
arr == sorted(arr)
