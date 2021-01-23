'''
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)

递归
'''
import sys
sys.path.append(r"C:\Documents\GitHub\Data-Structure-and-Algorithms")
from BST.BinarySearchTree import Tree

class Solution:
    def findPath(self, root, integer):
        result = []

        def find(root, sum, path=None):
            if path == None: path = []
            if not root: return []     # NULL
            path.append(root)
            if root.leftChild == None and root.rightChild == None and root.value == sum:
                # hit in leaf nodes
                onepath = []
                for node in path:
                    onepath.append(node.value)
                result.append(onepath)
            else:
                if root.leftChild:
                    find(root.leftChild, sum-root.value, path)
                if root.rightChild:
                    find(root.rightChild, sum-root.value, path)
            path.pop()
        
        find(root, integer)
        return result

bst = Tree()
ls = [10,5,2,4,7,11]
for i in ls:
    bst.insert(i)

s = Solution()
print(s.findPath(bst.root, 21))