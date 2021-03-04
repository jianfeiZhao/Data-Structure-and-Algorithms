import sys
sys.path.append(r"C:\Documents\GitHub\Data-Structure-and-Algorithms")
from Huffman.minHeap import MinHeap

class TreeNode:
    def __init__(self, x):
        self.freq = x
        self.left = None
        self.right = None

class HuffmanTree:
    def huffman(self, ls):
        n = len(ls)
        Q = MinHeap(ls)
        for i in range(n-1):
            leftNode = TreeNode(Q.extractMin())
            rightNode = TreeNode(Q.extractMin())
            parent = TreeNode(leftNode.freq+rightNode.freq)
            parent.left = leftNode
            parent.right = rightNode
            Q.Insert(parent.freq)
        return parent.freq


ls = [5,3,17,14,45,29]
tree = HuffmanTree()
print(tree.huffman(ls))