'''
给定一个二叉树，返回该二叉树层序遍历的结果，（从左到右，一层一层地遍历）
例如：
给定的二叉树是{3, 9,20, #,#,15,7},
该二叉树层序遍历的结果是[[3],[9,20],[15,7]] 
'''
class Solution:
    def levelOrder(self , root ):
        # write code here
        if not root: return []
        q = [root]
        res = []
        while q:
            level = len(q)
            sub = []
            for i in range(level):
                node = q.pop(0)
                sub.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(sub)
        return res