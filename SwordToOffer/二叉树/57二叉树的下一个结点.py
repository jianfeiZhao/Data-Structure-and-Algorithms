'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。

中序遍历的遍历顺序是 左 -> 根 -> 右。
1，二叉树为空，则返回空
2，当前节点的右子树存在，返回右子树的最左节点
3，当前节点的右子树不存在，则找第一个当前节点是父节点左孩子的节点
'''
import sys
sys.path.append(r"C:\Documents\GitHub\Data-Structure-and-Algorithms")
from BST.BinarySearchTree import Tree, Node

class Solution:
    def findParent(self, node, root):
        if root.rightChild != None:
            if root.rightChild == node:
                return root

        if root.leftChild != None:
            if root.leftChild == node:
                return root

        if root.value > node.value:
            return self.findParent(node, root.leftChild)
        if root.value < node.value:
            return self.findParent(node, root.rightChild)
        return None

    def findSuccessor(self, node, root):
        node_p = self.findParent(node, root)
        if node.value < node_p.value:
            node = node_p.leftChild
        else:
            node = node_p.rightChild
        #print(node.value)

        if not node or not root:
            return None
        if node.rightChild:      # has rightChild
            succ = node.rightChild
            while succ.leftChild:
                succ = succ.leftChild
            return succ
        else:      # no rightChild, go back to root and find the parent node of which is leftChild
            while self.findParent(node, root)!=None:
                if self.findParent(node, root).leftChild == node:
                    return self.findParent(node, root)
                node = self.findParent(node, root).value
        return None

def main():
    s = Solution()
    bst = Tree()
    ls = [10,6,7,8,13,12]
    for i in ls:
        bst.insert(i)
    
    root = bst.root
    print(s.findSuccessor(bst.find(7), root).value)
    print(s.findSuccessor(bst.find(8), root).value)
    print(s.findSuccessor(bst.find(12), root).value)
	
if __name__ == '__main__':
    main()