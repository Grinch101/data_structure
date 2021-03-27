# Heap


class Node:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"

    def __lt__(self, other):
        return self.value < other.value
#######################################################


class Heap:
    def __init__(self, lst):
        self._list = []
        for i in lst:
            self._list.append(Node(i))
        self._heapsize = len(self._list)
        self._build_heap()

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _is_heap(self):
        
        right_presence_check = lambda index: self._right(index) <= self._heapsize
        right_inequlity_check = lambda index: self._list[self._right(index)] < self._list[index]
        
        left_presence_check = lambda index: self._left(index) <= self._heapsize
        left_inequlity_check = lambda index: self._list[self._left(index)] < self._list[index]
        
        output = True
        for index in reversed(range(0, len(self._list)//2)):
            if right_presence_check(index):
                if not right_inequlity_check(index):
                    output = False
                    break
            if left_presence_check(index):
                if not left_inequlity_check(index):
                    output = False
                    break
            else:
                continue
                    
        return output
    
        
    def _max_heapify(self, index):
        if self._left(index) <= self._heapsize - 1:
            if self._list[self._left(index)] < self._list[index]:
                largest = index
            else:
                largest = self._left(index)

        if self._right(index) <= self._heapsize - 1:
            if self._list[self._right(index)] > self._list[largest]:
                largest = self._right(index)

        if self._right(index) <= self._heapsize - 1 or self._left(index) <= self._heapsize - 1:
            if largest != index:  # if true: store/ swap the largest value with index
                self._list[index], self._list[largest] = self._list[largest], self._list[index]
                # check the same situation down the tree
                self._max_heapify(largest)

    def _build_heap(self):
        for i in reversed(range(0, len(self._list)//2) ):
            self._max_heapify(i)
            
            
    def _parent_heapify(self,index):
        
        def find_parent(index):
            if_right = (index - 2) / 2
            if_left = (index - 1) / 2
            if if_right== round(if_right):
                return int(if_right)
            elif if_left == round(if_left):
                return int(if_left)
            
        parent = find_parent(index)
        if parent >=0:
            self._max_heapify(parent)
            self._parent_heapify(parent)
            
    def insert(self, val):
        self._list.append(Node(val))
        self._parent_heapify(index = len(self._list) - 1)


    def heapsort(self, inplace = True): # this function is messing with the state! book's order!
        from collections import deque
        
        if inplace == True:
            if self._is_heap():
                heapsort_array = deque()

                for i in reversed(range(0, len(self._list))):
                    heapsort_array.appendleft(self._list[0])
                    self._list[i], self._list[0] = self._list[0], self._list[i]
                    self._max_heapify(0)

                return heapsort_array
            else:
                self._build_heap()
                self.heap_sort()

        if inplace == False:
            sorted_array = self.heap_sort(inplace = True)
            self._build_heap()
            return sorted_array

    
    def maximum(self):
        self._build_heap()
        return self._list[0]

    def extract_maximum(self):
        if self._heapsize < 1:
            raise Exception('Heap underflow!')
        
        max_node = self.maximum()
        self._list[0] = self._list[self._heapsize - 1]
        self._list = self._list[0:-1]
        self._max_heapify(0)
        return max_node
    
    def __repr__(self):
        return f'{list(self._list)}'


myheap = Heap([1, 2, 3, 9, 0, 25])

print(myheap)
