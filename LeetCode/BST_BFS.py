'''
重建二叉树+二叉树的最小高度
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.dis = 9999

    def rebuildBST(self, pre, ino):
        if not pre: return None

        root = TreeNode(pre[0])
        pos = ino.index(pre[0])
        root.left = self.rebuildBST(pre[1:pos+1], ino[:pos])
        root.right = self.rebuildBST(pre[pos+1:], ino[pos+1:])
        return root

    def minHeightBST(self, root):
        q = []   # visited
        root.dis = 1
        while root.left or root.right:
            if root.left:
                root.left.dis = root.dis + 1
                q.append(root.left)
            if root.right:
                root.right.dis = root.dis + 1
                q.append(root.right)
            root = q.pop(0)
        return root.dis
