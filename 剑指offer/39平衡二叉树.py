'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

需要用到查找二叉树深度的函数，根据平衡二叉树的性质：它是一棵空树或它的左右两个子树的高度差不超过1，
并且左右两个子树都是一棵平衡二叉树，递归求解。
'''
import sys
sys.path.append(r"C:\Documents\GitHub\Data-Structure-and-Algorithms")
from BST.BinarySearchTree import Tree, Node

class Solution:
    def isBalancedBST(self, root):
        if not root: return True

        if root.leftChild:
            left = root.leftChild.getHeight()
        else:
            left = 0

        if root.rightChild:
            right = root.rightChild.getHeight()
        else:
            right = 0

        if abs(left-right) <= 1:
            return self.isBalancedBST(root.leftChild) and self.isBalancedBST(root.rightChild)
        else:
            return False


s = Solution()
bst = Tree()
ls = [10,5,2,7,11,14]
for i in ls:
    bst.insert(i)
print(s.isBalancedBST(bst.root))

bst.insert(16)
print(s.isBalancedBST(bst.root))