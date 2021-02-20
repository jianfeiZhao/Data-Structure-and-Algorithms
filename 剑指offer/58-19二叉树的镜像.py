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

'''
判断二叉树是不是对称的。如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''
class Solution:
    def isSymmetrical(self, root):
        if root == None:
            return True
        return self.isBalance(root.leftChild, root.rightChild)

    def isBalance(self, left, right):
        if (left==None)and(right==None):      # reach to the leafnode
            return True
        if ((left==None)and(right!=None))or((left!=None)and(right==None)):
            return False
        if left.val != right.val:
            return False
        return self.isBalance(left.rightChild,right.leftChild) and self.isBalance(left.leftChild,right.rightChild)


# build the BST
tree = Tree()
ls = [10,5,2,7,11,14]
for i in ls:
    tree.insert(i)
print(tree.preorder())

s = Solution()
s.BSTMirror(tree.root)
print(tree.preorder())