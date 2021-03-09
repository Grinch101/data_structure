def BinarySearch(arr, item):
    if item > arr[-1] or item < arr[0]:
        print( 'Not present' )
        return
    else:    
        mid_len = round(len(arr)/2 )
        if item == arr[mid_len]:
            print('Present')
            return 

        elif item > arr[mid_len]:
            BinarySearch(arr[mid_len:] , item)

        elif item < arr[mid_len]:
            BinarySearch(arr[:mid_len] , item)

