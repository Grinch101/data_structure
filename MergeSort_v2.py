
def merge_sort( arr):
    if len(arr) >= 2:

        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = idx = 0
        while True:
            if left[i] <= right[j]:
                arr[idx] = left[i]
                idx += 1
                i += 1
                if i == len(left):
                    break
            else:
                arr[idx] = right[j]
                idx += 1
                j += 1
                if j == len(right):
                    break

        # put extra item(s) in arr
        while i < len(left):
            arr[idx] = left[i]
            idx += 1
            i += 1
        while j < len(right):
            arr[idx] = right[j]
            idx += 1
            j += 1
    return arr

# test:

mg = merge_sort([9, 6, 4, 2, 0, 3, 1, 7, 8])
print(mg)
