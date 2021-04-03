
class INT(int):

    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(str(self.data))
