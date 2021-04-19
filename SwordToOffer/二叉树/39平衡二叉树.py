'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

需要用到查找二叉树深度的函数，根据平衡二叉树的性质：它是一棵空树或它的左右两个子树的高度差不超过1，
并且左右两个子树都是一棵平衡二叉树，递归求解。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def getHeight(self):
        if self.left and self.right:
            return 1 + max(self.left.getHeight(), self.right.getHeight())
        
        elif self.left:
            return 1 + self.left.getHeight()

        elif self.right:
            return 1 + self.right.getHeight()
        
        else:
            return 1

class Solution:
    def isBalancedBST(self, root):
        if not root: return True

        if root.left:
            left = root.left.getHeight()
        else:
            left = 0

        if root.right:
            right = root.right.getHeight()
        else:
            right = 0

        if abs(left-right) <= 1:
            return self.isBalancedBST(root.left) and self.isBalancedBST(root.right)
        else:
            return False
