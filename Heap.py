# Heap


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.right_child = None
        self.left_child = None
        
    def __repr__(self):
        return f"{self.value}"


class Heap:
    def __init__(self):
        self._hash = {}
    
    def _left(self,i):
        return 2 * i
    
    def _right(self,i):
        return 2 * i + 1
        
    def get_list(self, lst):
        for i , item in enumerate(lst, start=1):
            self._hash[i] = Node(item)

        self._build_heap()
    

    def _max_heapify(self , index):
        
        heap_size = len(self._hash) 

        if self._left(index) <= heap_size:
            if self._left(index) <= heap_size and self._hash[self._left(index)].value < self._hash[index].value:
                largest = index
            else:
                largest = self._left(index) # so far, the largest value has stored in the left child 

        if self._right(index) <= heap_size:
            if self._right(index) <= heap_size and self._hash[self._right(index)].value > self._hash[largest].value:
                largest = self._right(index)
        
        if self._right(index) <= heap_size or self._left(index) <= heap_size:
            if largest != index: #if true: store/ swap the largest value with index
                self._hash[index] , self._hash[largest] = self._hash[largest] , self._hash[index]

                self._max_heapify(largest) # check the same situation down the tree

    

    def _build_heap(self):
        for i in reversed(range(1 , len(self._hash)//2 + 1) ):
            
            self._max_heapify(i)
        
        
    def __repr__(self):
        return f'{list(self._hash.values())}'