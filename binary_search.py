########## Binary search ############
# Recursively find an item in an sorted array
## devide the array into half until the len of array is 1 and the item is found.
## worst  omplexity O(n)
## general complexity O(h) - h is the height of the tree
def binary_search(arr, item, upper_ind = None, lower_ind = None):

    if upper_ind == None or lower_ind == None:
        upper_ind = len(arr) - 1
        lower_ind = 0

    if item > arr[upper_ind] or item < arr[lower_ind]:
        return False

    else:
        mid_ind = round((lower_ind + upper_ind)/2)

        if item == arr[mid_ind]:
            return mid_ind

        elif item > arr[mid_ind]:
            binary_search(arr, item, upper_ind, mid_ind + 1)

        elif item < arr[mid_ind]:
            binary_search(arr, item, mid_ind - 1, lower_ind)
