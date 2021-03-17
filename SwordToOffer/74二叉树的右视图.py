'''
请根据二叉树的前序遍历，中序遍历恢复二叉树，并打印出二叉树的右视图
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def solve(self , pre , ino ):
        # write code here
        if not pre and not ino:
            return []
         
        houxu = []
        root = self.get_tree(pre, ino)
         
        if not root:
            return []
         
        queue = [root]
        res = []
        tmp = []
        while queue:
            sub = []
            node = queue.pop(0)
            sub.append(node.val)
            if node.left :
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)

            if not queue:
                res.append(sub[-1])
                queue = tmp
                tmp = []
        return res
                 
    def get_tree(self, pre, ino):
        if not pre:
            return None

        root = ListNode(pre[0])
        index = ino.index(root.val)
         
        root.left = self.get_tree(pre[1:index+1], ino[:index])
        root.right = self.get_tree(pre[index+1:], ino[index+1:])
        return root