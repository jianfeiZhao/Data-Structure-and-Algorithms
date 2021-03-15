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

'''
给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）
例如：
给定的二叉树是{3,9,20,#,#,15,7},
该二叉树之字形层序遍历的结果是[[3],[20,9],[15,7]]
'''
class Solution:
    def zigzagLevelOrder(self , root ):
        # write code here
        if not root: return []
        # 用两个stack分别存奇偶行
        q1 = [root]
        q2 = []
        res = []
        while q1 or q2:
            sub = []
            while q1:
                node = q1.pop()
                sub.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            if len(sub)>0:
                res.append(sub)
                sub = []
            while q2:
                node = q2.pop()
                sub.append(node.val)
                if node.right:
                    q1.append(node.right)
                if node.left:
                    q1.append(node.left)
            if len(sub)>0:
                res.append(sub)
                sub = []
        return res