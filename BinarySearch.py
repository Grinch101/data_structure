def BinarySearch(arr, item, upper_ind=None, lower_ind=None):

    if upper_ind == None or lower_ind == None:
        upper_ind = len(arr) - 1
        lower_ind = 0

    if item > arr[upper_ind] or item < arr[lower_ind]:
        return False

    else:
        mid_ind = round((lower_ind + upper_ind)/2)

        if item == arr[mid_ind]:
            print(mid_ind)
            return mid_ind

        elif item > arr[mid_ind]:
            BinarySearch(arr, item, upper_ind, mid_ind+1)

        elif item < arr[mid_ind]:
            BinarySearch(arr, item, mid_ind-1, lower_ind)
