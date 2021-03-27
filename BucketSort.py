
def bucket_sort(arr, max_int=None):

    import numpy as np
    arr = np.array(arr)

    if max_int is None:
        max_int = arr.max()
    arr = arr / (max_int+1)  # standardize

# Auxiliaries:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return f'{self.data}'

        def __lt__(self, other):
            return self.data < other.data

    class LinkedList:
        def __init__(self):
            self.head = None

        def add(self, val):
            node = Node(val)
            if self.head is None:
                self.head = node
            else:
                temp = self.head
                self.head = node
                node.next = temp

        def sort(self):
            def insertion_sort(A):
                for i in range(1, len(A)):
                    for j in range(i-1, -1, -1):
                        if A[j] > A[j+1]:
                            A[j], A[j+1] = A[j+1], A[j]
                        else:
                            break
                return A

            lst = self._to_lst()
            return insertion_sort(lst)

        def _to_lst(self):
            lst = []
            cur_node = self.head
            while cur_node is not None:
                lst.append(cur_node.data)
                if cur_node.next is None:
                    break
                else:
                    cur_node = cur_node.next
            return lst

    # create 10 buckets:
    buckets = [LinkedList() for i in range(0, 10)]

    # determine each item's bucket and assign it to that:
    sorted_vals = []
    i = 0
    while i < len(arr):  # adding each item to its bucket
        n = int(arr[i] * 10)
        linked_list = buckets[n]
        linked_list.add(arr[i])
        i += 1

    for ll in buckets:  # investigating all the buckets ( which is 10 )
        ll = ll.sort()
        sorted_vals = sorted_vals + ll

    sorted_vals = np.array(sorted_vals) * (max_int+1)
    return list(sorted_vals)


# test
print(bucket_sort([99, 88, 1, 23], max_int=99))
print(bucket_sort([99, 88, 1, 23]))
