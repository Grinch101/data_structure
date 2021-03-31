### new_version of BST, rewritten by me / first commit

# Basic operations on a binary search tree take time proportional to the height of the tree.
# For a complete binary tree with n nodes, such operations run in O(log(n)) worst-case time.
# If the tree is a linear chain of n nodes, however, the same operations take O(n) worst-case time.

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.data < other.data
    
    def __eq__(self, other):
        return self.data == other.data
        
    def __gt__(self, other):
        return self.data > other.data
    
    def __ne__(self, other):
        return self.data != other.data

    def __repr__(self):
        return f"{self.parent} → {self.data}"
    

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):

        def _insert(cur_node, parent_node, node):
            if cur_node is None:
                if node < parent_node:
                    node.parent = parent_node
                    parent_node.left = node
                elif node == parent_node or node > parent_node:
                    node.parent = parent_node
                    parent_node.right = node

            else:
                if node < cur_node:
                    _insert(cur_node.left, cur_node, node)
                if node > cur_node or node == cur_node:
                    _insert(cur_node.right, cur_node, node)


        if self.root is None:
            self.root = Node(val)
            self.root.parent = None
        else:
            node = Node(val)
            if node < self.root:
                _insert(self.root.left, self.root, node)
            if node > self.root or node == self.root:
                _insert(self.root.right, self.root, node)
    
    @property
    def height(self):
        
        def _height(cur_node, direction, counter = 0):
        
            if cur_node is None:
                return counter

            if direction == 'right':
                return _height(cur_node = cur_node.right, direction='right', counter = counter + 1)
            if direction == 'left':
                return _height(cur_node = cur_node.left, direction='left', counter = counter + 1)

        if self.root is not None:
            return max( _height(self.root, 'left'), _height(self.root, 'right') )
        else:
            return "0: The tree is empty"

    @property
    def plot(self):
        def print_tree(root, val="data", left="left", right="right"):
            def _display(root, val=val, left=left, right=right):
                """Returns list of strings, width, height, and horizontal coordinate of the root."""
                # No child.
                if getattr(root, right) is None and getattr(root, left) is None:
                    line = '%s' % getattr(root, val)
                    width = len(line)
                    height = 1
                    middle = width // 2
                    return [line], width, height, middle

                # Only left child.
                if getattr(root, right) is None:
                    lines, n, p, x = _display(getattr(root, left))
                    s = '%s' % getattr(root, val)
                    u = len(s)
                    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                    second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                    shifted_lines = [line + u * ' ' for line in lines]
                    return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

                # Only right child.
                if getattr(root, left) is None:
                    lines, n, p, x = _display(getattr(root, right))
                    s = '%s' % getattr(root, val)
                    u = len(s)
                    first_line = s + x * '_' + (n - x) * ' '
                    second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                    shifted_lines = [u * ' ' + line for line in lines]
                    return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

                # Two children.
                left, n, p, x = _display(getattr(root, left))
                right, m, q, y = _display(getattr(root, right))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
                second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
                if p < q:
                    left += [n * ' '] * (q - p)
                elif q < p:
                    right += [m * ' '] * (p - q)
                zipped_lines = zip(left, right)
                lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
                return lines, n + m + u, max(p, q) + 2, n + u // 2

            lines, *_ = _display(root, val, left, right)
            for line in lines:
                print(line)
    
        root = self.root
        print_tree(root)

    def find(self, val):
        '''
        Return the Node if presents in the tree.
        "left" or "right"
        '''
        def _isin(cur_node, node):
            if cur_node is None:
                return False
            elif cur_node == node:
                return cur_node
            
            elif node < cur_node:
                return _isin(cur_node.left, node)
            else:
                return _isin(cur_node.right, node)

        cur_node = self.root
        node = Node(val)
        return _isin(cur_node, node)

    @property
    def max(self):
        
        def _max(cur_node):
            if cur_node.right is None:
                return cur_node.data
            else:
                return _max(cur_node.right)

        if self.root is None:
            return "The root is empty"
        return _max(self.root)

    @property
    def min(self):

        def _min(cur_node):
            if cur_node.left is None:
                return cur_node.data
            else:
                return _min(cur_node.left)

        if self.root is None:
            return "The tree is empty"
        else:
            return _min(self.root)

    def relation(self, child):
        '''
        Return the relationship of a child node with its parent
        '''
        if child.parent is None:
            return None
        parent = child.parent
        if parent.left:
            if parent.left == child:
                return 'left'
        if parent.right:
            if parent.right == child:
                return 'right'

    def delete(self, val):
               
        # case 1 - if node has no children:
        node = self.find(val)
        if node: # find the node
            
            parent_node = node.parent # find its parent
            if node.right is None and node.left is None: # if has no child
                if parent_node < node or node.parent == node:    # if the node to be deleted is the right node:
                    parent_node.right = None
                else:
                    parent_node.left = None
            
            # case 2 - if node has 1 child: (a left child)
            elif node.left is not None and node.right is None:
                attr = self.relation(node)
                setattr(parent_node, attr, node.left)

            #  if node has 1 child: (a right node)
            elif node.left is None and node.right is not None:
                attr = self.relation(node)
                setattr(parent_node, attr, node.right)

            ## if node has two children:
            # if node to be delete is a right child:
            elif node.left is not None and node.right is not None:
                # save parents and left child of the node
                LEFT = node.left
                PARENT = node.parent
                # disconnect its relation with other (left, parent):
                attr = self.relation(node)
                # introduce the new node:
                new_node = node.right
                # save the left branch before glueing to old LEFT - we need it for right node which is being shifted up:
                if new_node.left:
                    LEFT2 = new_node.left
                # inherit the removed node's relationship
                new_node.left = LEFT
                LEFT.parent = new_node
                new_node.parent = PARENT
                setattr(PARENT, attr, new_node)

                # iterativly we must connect push up right node by 1:
                if new_node.right:
                    X = new_node.right
                    while True: 
                        X.left = LEFT2 # right_node_number_2 inheriting the left from right_node_number_1
                        LEFT2.parent = X
                        
                        X.parent = new_node
                        LEFT2 = X.left
                        
                        if X.right is None or X.left is None:
                            break
                        X = X.right
        else:
            raise Exception( "Node not found!" )


############## test
BST = BinarySearchTree()
import random
import time
from os import system
cls = lambda: system('cls')
cls()
random.seed(11)
num = 50
for i in range(num):
    X = random.randint(0,200)
    BST.insert(X)
    print('X is',X)
    BST.plot
    time.sleep(0.008)
    if i < num - 1:
        cls()

BST.delete(177)
BST.plot

