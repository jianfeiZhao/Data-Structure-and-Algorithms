# Binary Search Tree in Python(assume all the value are unique)
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
    
    def getSize(self):
        if self.leftChild and self.rightChild:
            return 1 + self.leftChild.getSize() + self.rightChild.getSize()
        
        elif self.leftChild:
            return 1 + self.leftChild.getSize()

        elif self.rightChild:
            return 1 + self.rightChild.getSize()
        
        else:
            return 1

    def getHeight(self):
        if self.leftChild and self.rightChild:
            return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
        
        elif self.leftChild:
            return 1 + self.leftChild.getHeight()

        elif self.rightChild:
            return 1 + self.rightChild.getHeight()
        
        else:
            return 1

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def getSize(self):
        if self.root:
            return self.root.getSize()
        else:
            return 0

    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return 0
    
    def remove(self, data):
        # empty tree
        if self.root is None:
            return False
        
        # data is in root node
        elif self.root.value == data:
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.root.rightChild
            else:
                # find the successor
                parent = self.root
                succ = self.root.rightChild
                while succ.leftChild:
                    parent = succ
                    succ = succ.leftChild
                self.root.value = succ.value  # move the successor to root
                if succ.rightChild:           # successor has right child
                    if parent.value > succ.value:
                        parent.leftChild = succ.rightChild
                    else:
                        parent.rightChild = succ.rightChild
                else:                         # successor has no child
                    if parent.value > succ.value:
                        parent.leftChild = None
                    else:
                        parent.rightChild = None
            return True
        
        parent = None
        node = self.root

        # find node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.leftChild
            else:
                node = node.rightChild

        # case 1: data not found
        if node is None:
            return False
        
        # case 2: removed node has no children
        elif node.leftChild is None and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return True

        # case 3: removed node only has left child
        elif node.leftChild and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
            return True

        # case 4: removed node only has right child
        elif node.leftChild is None and node.rightChild:
            if data < parent.value:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return True

        # case 5: removed node has two children
        else:
            # find the successor
            parent = node
            succ = node.rightChild
            while succ.leftChild:
                parent = succ
                succ = succ.leftChild
            node.value = succ.value       # move the successor to removed node
            if succ.rightChild:           # successor has right child
                if parent.value > succ.value:
                    parent.leftChild = succ.rightChild
                else:
                    parent.rightChild = succ.rightChild
            else:                         # successor has no child
                if parent.value > succ.value:
                    parent.leftChild = None
                else:
                    parent.rightChild = None
        return True

    def preorder(self):    
        if self.root is not None:
            print('PreOrder')
            self.root.preorder()
    
    def postorder(self):
        if self.root is not None:
            print('PostOrder')
            self.root.postorder()
    
    def inorder(self):
        if self.root is not None:
            print('InOrder')
            self.root.inorder()

def main():
    bst = Tree()
    ls = [10,5,2,7,7,11,14]
    for i in ls:
        print(bst.insert(i))
    
    bst.preorder()
    bst.inorder()
    print('Height = ', bst.getHeight())
    print('Size = ', bst.getSize())
	#bst.postorder()
	#bst.inorder()
    print(bst.remove(10))
    bst.preorder()
	
if __name__ == '__main__':
    main()