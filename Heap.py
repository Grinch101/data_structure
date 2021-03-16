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
        self._heapsize = len(self._list) - 1
        self._build_heap()
        
        
    def _left(self,i):
        return 2 * i + 1
    
    def _right(self,i):
        return 2 * i + 2

    def _is_heap(self):
        index = 0
        while index <= len(self._list)//2:
            if self._right(index) <= self._heapsize and self._left(index) <= self._heapsize:
                if self._list[self._left(index)] < self._list[index] and self._list[self._right(index)] < self._list[index]:
                    index += 1
                else:
                    False
                    break
            else:
                False
                break
        return True
            
            
    
    def heap_sort(self):
        from collections import deque
        
        if self._is_heap():
            
            _heapsort_array = deque()


            for i in reversed(range(0, len(self._list))):

                _heapsort_array.appendleft(self._list[0])

                self._list[i] , self._list[0] = self._list[0], self._list[i]

                self._heapsize -= 1
                self._max_heapify(0)

            return _heapsort_array
        else: 
            self._max_heapify()
            self.heap_sort()


    def _max_heapify(self , index):
        
        if self._left(index) <= self._heapsize:
            if self._left(index) <= self._heapsize and self._list[self._left(index)] < self._list[index]:
                largest = index
            else:
                largest = self._left(index) # so far, the largest value has stored in the left child 

        if self._right(index) <= self._heapsize:
            if self._right(index) <= self._heapsize and self._list[self._right(index)] > self._list[largest]:
                largest = self._right(index)
        
        if self._right(index) <= self._heapsize or self._left(index) <= self._heapsize:
            if largest != index: #if true: store/ swap the largest value with index
                self._list[index] , self._list[largest] = self._list[largest] , self._list[index]

                self._max_heapify(largest) # check the same situation down the tree

    
    

    def _build_heap(self):
        for i in reversed(range(0 , len(self._list)//2 ) ):
            
            self._max_heapify(i)
        
        
    def __repr__(self):
        return f'{list(self._list)}'
        

myheap = Heap([1,2,3,9,0,25])

print(myheap)