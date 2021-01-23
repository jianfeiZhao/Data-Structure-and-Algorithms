'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

时间限制：1秒；空间限制：32768K

主要用到了递归的方法。第一步先遍历树A，找到和树B根节点值相同的节点A'；
第二步判断以A'为根节点的子树中是否包含树B。
'''
import sys
sys.path.append(r"C:\Documents\GitHub\Data-Structure-and-Algorithms")
from BST import Tree

class Solution:
    def SubTree(self, rootA, rootB):
        result = False
        if rootA!=None and rootB!=None:
            if rootA.value == rootB.value:
                result = self.iscomprise(rootA, rootB)
            if result != True:
                result = self.SubTree(rootA.leftChild, rootB)
            if result != True:
                result = self.SubTree(rootA.rightChild, rootB)
        return result

    def iscomprise(self, rootA, rootB):
        if rootB == None:
            return True
        if rootA == None:
            return False
        #if rootA.value != rootB.value:
            #return False
        if rootA.value == rootB.value:
            return self.iscomprise(rootA.leftChild, rootB.leftChild) and \
                self.iscomprise(rootA.rightChild, rootB.rightChild)

# build the BST
tree1 = Tree()
ls = [10,5,2,7,11,14]
for i in ls:
    tree1.insert(i)

tree2 = Tree()
ls = [5,2,7]
for i in ls:
    tree2.insert(i)

tree3 = Tree()
ls = [5,3,7]
for i in ls:
    tree3.insert(i)

s = Solution()
print(s.SubTree(tree1.root, tree2.root))     # True
print(s.SubTree(tree1.root, tree3.root))     # False