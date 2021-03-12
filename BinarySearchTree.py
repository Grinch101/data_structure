class Node:
    def __init__(self, value = None):
        self.value = value
        self.big_child = None
        self.little_child = None

        
class BST:
    def __init__(self):
        self.root = None
        self.test_list = [] ####### for test
    
    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
        
    def _insert(self,value, current_node):
        if value < current_node.value:
            if current_node.little_child == None:
                current_node.little_child = Node(value)
            else:
                self._insert(value, current_node.little_child) # recursion
        if value > current_node.value:
            if current_node.big_child == None:
                current_node.big_child = Node(value)
            else:
                self._insert(value, current_node.big_child)
        else:
#             raise Exception('Duplicate Value')
            pass
            
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
        else:
            print('No tree to show')
            
    def _print_tree(self,current_node):
        if current_node != None:
            self._print_tree(current_node.little_child)
            print(str(current_node.value))
            self.test_list.append(current_node.value)   ####### for test
            self._print_tree(current_node.big_child)

    
    def height(self):
        if self.root != None:
            self._height(self.root, 0)
        else:
            print("The height is 0")
            return "The height is 0"
        
    def _height(self, current_node, current_height):
        
        if current_node == None: 
            print(current_height) ####### for test
            return current_height
        
        else:
            left_height = self._height(current_node.little_child , current_height+1)
            right_height = self._height(current_node.big_child , current_height+1)
            return max(left_height, right_height)


def test():
    import random

    mytree = BST()

    lst = [i for i in range(0,20)]

    while True:
        try:
            val = lst.pop(random.randint(0,20))
            mytree.add(val)
            if len(lst)<1:
                break
        except:
            pass
    
    sorted_nodes = mytree.test_list
    
    return sorted(sorted_nodes) == sorted_nodes


test()