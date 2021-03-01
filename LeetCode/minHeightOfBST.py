
class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
        self.dis = 9999

class Solution:
    def minHeight(self, root):
        visit = []
        root.dis = 1
        while root.leftChild or root.rightChild:
            if root.leftChild:
                root.leftChild.dis = root.dis + 1
                visit.append(root.leftChild)
            if root.rightChild:
                root.rightChild.dis = root.dis + 1
                visit.append(root.rightChild)
            root = visit.pop(0)
        return root.dis

# build the BST
node1 = Node(10)
node2 = Node(5)
node3 = Node(11)
node4 = Node(14)
node1.leftChild = node2
node1.rightChild = node3
node3.rightChild = node4

s = Solution()
print(s.minHeight(node1))   # 2

node5 = Node(2)
node6 = Node(7)
node2.leftChild = node5
print(s.minHeight(node1))   # 3
node2.rightChild = node6
print(s.minHeight(node1))   # 3