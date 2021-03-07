class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    
    def __repr__(self):
        return f"{self.data}"
        


class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for item in nodes:
                
                node.next = Node(item)
                node = node.next
                
    def remove(self, target_node):
        if self.head is None:
            raise Exception('Linked list is empty')

        if self.head == target_node:
            self.head = None
        
        node = self.head
        while node is not None:
            first_node = node
            second_node = self.head.next
            if second_node is not None and second_node == target_node:
                first_node.next = second_node.next
            
            node = node.next

                
    def add_left(self, node):
        node.next = self.head
        self.head = node
    
    def add_right(self, new_node):
        node = self.head
        while True:
            next_node = node.next
            if next_node == None:
                node.next = new_node
                break
            else:
                node = node.next
    
    def pop_left(self):
        if self.head is None:
            raise Exception('Linked list is empty')
        old_head = self.head
        self.head = self.head.next # new head
        return old_head
    
    def pop_right(self):
        if self.head is None:
            raise Exception('Linked list is empty')
        node = self.head
        while True:
            if node.next is not None:
                node = node.next
            else:
                output = node
                self.remove(node)
                break
        return output
        
                
            
        
    def __iter__(self):
        node = self.head
        cond = True
        while node is not None:
            yield node
            node = node.next
        
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    
    
