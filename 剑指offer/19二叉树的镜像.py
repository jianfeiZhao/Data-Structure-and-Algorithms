'''
输入给定的二叉树，将其变换为原二叉树的镜像。

交换左右子节点，递归
'''
import sys
sys.path.append(r"C:\Documents\GitHub\Data-Structure-and-Algorithms")
from BST import Tree

class Solution:
    def BSTMirror(self, root):
        if root == None:
            return
        root.leftChild, root.rightChild = root.rightChild, root.leftChild
        self.BSTMirror(root.leftChild)
        self.BSTMirror(root.rightChild)
        return


# build the BST
tree = Tree()
ls = [10,5,2,7,11,14]
for i in ls:
    tree.insert(i)
print(tree.preorder())

s = Solution()
s.BSTMirror(tree.root)
print(tree.preorder())