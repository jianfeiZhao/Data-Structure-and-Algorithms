# Binary Search Tree in Python
class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            return False

        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True

        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def getHeight(self):
        