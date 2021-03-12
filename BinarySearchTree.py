class Node:
    def __init__(self, value=None):
        self.value = value
        self.right_child = None
        self.left_child = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None
        self.test_list = []  # for test

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child = Node(value)
                current_node.left_child.parent = current_node
            else:
                self._insert(value, current_node.left_child)

        if value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = Node(value)
                current_node.right_child.parent = current_node
            else:
                self._insert(value, current_node.right_child)
        else:
            #             raise Exception('Duplicate Value')
            pass

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
        else:
            print('No tree to show')

    def _print_tree(self, current_node):
        if current_node != None:
            self._print_tree(current_node.left_child)
            print(str(current_node.value))
            self.test_list.append(current_node.value)  # for test
            self._print_tree(current_node.right_child)

    def height(self):
        if self.root != None:
            self._height(self.root, 0)
        else:
            print("The height is 0")
            return "The height is 0"

    def _height(self, current_node, current_height):

        if current_node == None:
            print(current_height)  # for test
            return current_height

        else:
            left_height = self._height(
                current_node.left_child, current_height+1)
            right_height = self._height(
                current_node.right_child, current_height+1)
            return max(left_height, right_height)

    def search(self, val):
        if self.root is None:
            return False
        else:
            self._search(self.root, val)

    def _search(self, current_node, val):
        if current_node.value == val:
            return True

        elif current_node.left_child != None and val < current_node.value:
            return self._search(current_node.left_child, val)

        elif current_node.right_child != None and val > current_node.value:
            return self._search(current_node.right_child, val)

        else:
            return False

    def find(self, val):  # this function returns the Node of a given value
        if self.root != None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, current_node):
        if val == current_node.value:
            return current_node
        elif val < current_node.value and current_node.left_child != None:
            return self._find(val, current_node.left_child)
        elif val > current_node.value and current_node.right_child != None:
            return self._find(val, current_node.right_child)

    def delete_val(self, val):
        return self.delete_node(self.find(val))

    def delete_node(self, node):
        if not self.search(node):
            print('Not present')
            return

        ## Helpers:
        def _min_value_node(node):
            current = node
            while current.left_child != None:
                current = current.left_child
            return current # returns the smallest node after the given node
        
        def _num_child(node):
            counter = 0
            if node.left_child != None:
                counter += 1
            if node.right_child != None:
                counter += 1
            return counter

        # we have 3 cases:
        num_children = _num_child(node)
        parent_node = node.parent
        ## case 1:
        ### deleting leaf node: _num_child = 0 
        if num_children == 0:
            if parent_node.left_child == node:
                parent_node.left_child = None
            else:
                parent_node.right_child = None

        ## case 2:
        ### deleting a node with only 1 child:
        if num_children == 1:
            if node.right_child != None:
                child = node.left_child # store the orphan
            else:
                child = node.right_child
            
            if parent_node.right_child == node: # drop the orphon on its grannies hands
                parent_node.right_child = child
            else:
                parent_node.left_child = child

            child.parent = parent_node # remove the parent's name with its grannies

        ## case 3:
        ### deleting a node with two child:
        if num_children == 2:
            # get the successor of the deleted node
            successor=_min_value_node(node.right_child)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value=successor.value

            # delete the inorder successor now that it's value was
            # copied into the other node
            self.delete_node(successor)


def test():
    import random

    mytree = BST()

    lst = [i for i in range(0, 20)]

    while True:
        try:
            val = lst.pop(random.randint(0, 20))
            mytree.add(val)
            if len(lst) < 1:
                break
        except:
            pass


    mytree.print_tree()

    for i in mytree.test_list:
        assert mytree.search(i) == True , "Value is not in the tree"
        mytree.delete_val(i)
        assert mytree.search(i) == False , "Value hasn't been deleted"
    print('All good!')

test()