# LinkedList:
# To search a list of n objects, the LIST-SEARCH procedure takes O(n) time in the worst case, since it may have to search the entire list.
# The running time for LISTINSERT on a list of n elements is O(1).
## LIST-DELETE runs in O(1) time, but if we wish to delete an element with a given key,
## O(n) time is required in the worst case because we must first call LIST-SEARCH to find the element.

from Node import Node

class LinkedList:
    def __init__(self, vals = None):
        self.head = None

        if type(vals) == list:
            head = Node(vals.pop(0))
            self.head = head
            for item in vals:
                self.add_left(item)


    
    def remove(self, item, type='int'):
        if type == "Node":
            val = item.data
        else:
            val = item
        
        if self.head is None:
            raise Exception('Linked list is empty')

        elif self.head.data == val:
            self.head = self.head.next
        
        else:
            node = self.head
            while node is not None:
                first_node = node
                second_node = first_node.next
                if second_node is not None and second_node.data == val:
                    first_node.next = second_node.next
                    break
                node = node.next

    def add_left(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
    
    def add_right(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            node = self.head
            while True:
                if node.next is None:
                    node.next = Node(val)
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
            if node.next is None:
                output = node
                self.remove(node, type='Node')
                break
            else:
                node = node.next
                
        return output
        
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        
    def __repr__(self):

        output =  f'{self.head}'
        node = self.head
        while node is not None:
            output = output + f" →  {node.data}"
            node = node.next
        return output
    
########## debug
# ll = LinkedList([1,2,3,4,5])
# print(ll)
# ll.add_right(222)
# print(ll)
# ll.add_left('left')
# print(ll)
# ll.remove(3)
# print(ll)
# ll.pop_left()
# print(ll)
# ll.pop_right()
# print(ll)
