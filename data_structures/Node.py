class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   

    def __repr__(self):
        return f"{self.data}"

    def __lt__(self, other):
            return self.data < other.data
    
    def __eq__(self, other):
        return self.data == other.data
        
    def __gt__(self, other):
        return self.data > other.data
    
    def __ne__(self, other):
        return self.data != other.data
    
    def __ge__(self, other):
        return self.data >= other.data
    
    def __le__(self, other):
        return self.data <= other.data
        