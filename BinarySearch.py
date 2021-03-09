def BinarySearch(arr, item, upper_ind=None, lower_ind=None):

    if upper_ind == None or lower_ind == None:
        upper_ind = len(arr) - 1
        lower_ind = 0

    if item > arr[upper_ind] or item < arr[lower_ind]:
        print('False')
        return False

    else:
        mid_ind = round((lower_ind + upper_ind)/2)

        if item == arr[mid_ind]:
            print(mid_ind)
            return mid_ind

        elif item > arr[mid_ind]:
            upper_ind = (len(arr[mid_ind:upper_ind]) + 1) + mid_ind
            BinarySearch(arr, item, upper_ind=upper_ind, lower_ind=mid_ind)

        elif item < arr[mid_ind]:
            lower_ind = mid_ind - (len(arr[lower_ind:mid_ind]) + 1)
            BinarySearch(arr, item, upper_ind=mid_ind, lower_ind=lower_ind)
