# Heap


class Node:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class Heap:
    def __init__(self):
        self._list = []
    
    def _left(self,i):
        return 2 * i + 1
    
    def _right(self,i):
        return 2 * i + 2
        
    def get_list(self, lst):
        for i in lst:
            self._list.append(Node(i))

        self._build_heap()
    

    def _max_heapify(self , index):
        
        heap_size = len(self._list) -1 

        if self._left(index) <= heap_size:
            if self._left(index) <= heap_size and self._list[self._left(index)].value < self._list[index].value:
                largest = index
            else:
                largest = self._left(index) # so far, the largest value has stored in the left child 

        if self._right(index) <= heap_size:
            if self._right(index) <= heap_size and self._list[self._right(index)].value > self._list[largest].value:
                largest = self._right(index)
        
        if self._right(index) <= heap_size or self._left(index) <= heap_size:
            if largest != index: #if true: store/ swap the largest value with index
                self._list[index] , self._list[largest] = self._list[largest] , self._list[index]

                self._max_heapify(largest) # check the same situation down the tree

    

    def _build_heap(self):
        for i in reversed(range(0 , len(self._list)//2 ) ):
            
            self._max_heapify(i)
        
        
    def __repr__(self):
        return f'{list(self._list)}'
        

myheap = Heap()

myheap.get_list([1,2,3,9,0,25])

print(myheap)