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
        self._list = []
        
    def get_list(self, lst):
        for i in lst:
            self._list.append(Node(i))
        self._max_heapify()
    
    
    def _max_heapify(self):
        
        for index in range(0,len(self._list)//2):
            
            cur_node = self._list[index]
            left_child = self._list[2*index]
            right_child = self._list[2*index + 1]
            
            nodes_values = [cur_node.value , right_child.value, left_child.value]
            largest_node = Node(nodes_values.pop(nodes_values.index(max(nodes_values)))) # :)))) fohsh nade!
            
            self._list[index] = largest_node
            self._list[2*index] = Node(nodes_values.pop())
            self._list[2*index + 1] = Node(nodes_values.pop())
    
    def __repr__(self):
        return self._list