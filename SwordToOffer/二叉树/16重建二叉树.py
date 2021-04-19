'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
import sys
sys.path.append(r"C:\Documents\GitHub\Data-Structure-and-Algorithms")
from BST.BinarySearchTree import Tree, Node
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
class Solution:
    # 返回构造的TreeNode根节点
    def reconstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        root = Node(pre[0])
        pos = tin.index(pre[0]) ### 根节点在中序遍历中的index，看作左子树的节点个数
        root.leftChild = self.reconstructBinaryTree(pre[1:1+pos], tin[:pos])   # 左子树
        root.rightChild = self.reconstructBinaryTree(pre[pos+1:], tin[pos+1:])   # 右子树
        return root

preorder = [10,5,2,7,11,14]
inorder = [2,5,7,10,11,14]
# test
s = Solution()
root = s.reconstructBinaryTree(preorder, inorder)
tree = Tree()
tree.root = root
print(tree.postorder())  # == [2,7,5,14,11,10]
