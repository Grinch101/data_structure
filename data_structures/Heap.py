# Heap
# The (binary) heap data structure is an array object that we can view as "a nearly complete binary tree"
# Eachnode of the tree corresponds to an element of the array
# An array condition that represents a heap is an object with two attributes:
### condition:length, which (as usual) gives the number of elements in the array, and
### condition:heap-size, which represents how many elements in the heap are stored within array condition.
### That means: although condition[1:condition.length] may contain numbers, only the elements in condition[1:condition.heapsize],
###  where 0 ≤ condition.heapsize ≤ condition.length are valid elements of the heap.

# We have two kinds of Heap; 
## Min heap which condition[parent(i)] ≤ condition[i] and Max heap which is reverse
## that is to say, in the max heap the root value is the maximum val in entire tree, and vice versa for min heap.

# Maxheapify runs in O(log(n))
# Build max Heap runs in O(n)
## The HEAPSORT procedure, which runs in O(nlog(n)) time, sorts an array in place.
## since the call to BUILD-MAXHEAP takes time O(n) and each of the n - 1 calls to MAX-HEAPIFY takes time O(log(n)).
# The MAX-HEAP-INSERT, HEAP-EXTRACT-MAX, HEAP-INCREASE-KEY,and HEAP-MAXIMUM procedures, which run in O(log(n)) time,
# allow the heap data structure to implement a priority queue.



class Heap:
    def __init__(self, list_of_vals):
        self.list = []
        for item in list_of_vals :
            self.list.append(item)
        self.build_heap()

    def right(self, index, feature = 'index'):
        if feature == 'index':
            return index * 2 + 2

        if feature == 'value':
            if index * 2 + 2 < len(self.list):
                return self.list[index * 2 + 2]
            else:
                return False
        
        if feature == 'index value':
            if index * 2 + 2 < len(self.list):
                return self.right(index , feature = 'value') < self.list[index]
            else:
                return True
        
    def left(self, index, feature = 'index'):
        if feature == 'index':
            return index * 2 + 1

        if feature == 'value':
            if (index * 2 + 1) < len(self.list):
                return self.list[index * 2 + 1]
            else:
                return False
        
        if feature == 'index value': # presence of the index and inequality check between its parents
            if index * 2 + 1 < len(self.list):
                return self.left(index , feature = 'value') < self.list[index]
            else:
                return True

    def is_heap(self):
        output = []
        for index in range(len(self.list)):
            output.append(self.left(index , 'index value'))
            output.append(self.right(index , 'index value'))
        return all(output) 

    def max_heapify(self, index):
        if self.left(index) <= len(self.list) - 1:
            if self.list[self.left(index)] < self.list[index]:
                largest = index
            else:
                largest = self.left(index)

        if self.right(index) <= len(self.list) - 1:
            if self.list[self.right(index)] > self.list[largest]:
                largest = self.right(index)

        if self.right(index) <= len(self.list) - 1 or self.left(index) <= len(self.list) - 1:
            if largest != index:  # if true: store/ swap the largest value with index
                self.list[index], self.list[largest] = self.list[largest], self.list[index]
                # check the same situation down the tree
                self.max_heapify(largest)
 
    def append(self, val):
        def _max_heapify_upwards(index):
            if index < 3:
                return
            else:
                ## right nodes are located in even indexes, and left nodes are in odd indexes:
                if index % 2 > 0:
                    parent = int((index - 1)/2)
                else:
                    parent = int((index - 2)/2)
            
                if not self.list[index] < self.list[parent]:
                    self.list[index] , self.list[parent] = self.list[parent] , self.list[index]
                    return _max_heapify_upwards(parent)
        
        self.list.append(val)
        index = len(self.list) - 1
        return _max_heapify_upwards(index)

    def build_heap(self):
        if not self.is_heap():
            for idx in range(len(self.list)//2 , -1 , -1):
                self.max_heapify(idx)

    def heapsort(self):
        heapsize = len(self.list) -1
        idx = heapsize
        arr = []
        while idx <= heapsize and idx >= 0:
            arr.append(self.list[0])
            self.list[0] , self.list[idx] = self.list[idx] , self.list[0]
            self.list.pop()
            heapsize -= 1
            idx -= 1
            self.max_heapify(0)

        return arr

    def max(self):
        return self.list[0]

    def pop_max(self):
        _max =  self.list.pop(0)
        self.max_heapify(0)
        return _max

    def __repr__(self):
        return f"{self.list}"




############### debug
myheap = Heap([9, 2, 3, 1, 25, 0])

myheap.append(24)
print(myheap.is_heap())
print(myheap)
print(myheap.max())
print(myheap.pop_max())
print(myheap)
# print(myheap.heapsort())
