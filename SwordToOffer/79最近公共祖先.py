'''
给定一棵二叉树以及这棵树上的两个节点 o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点。 

最近公共祖先和o1,o2有三种关系：
1. o1,o2分别在祖先左右两侧
2. 祖先是o1，o2在祖先左/右侧
3. 祖先是o2，o1在祖先左/右侧 

使用dfs深度遍历，如果节点为o1,o2其中一个直接返回，如果节点超过叶子节点也返回
'''
class Solution:
    def lowestCommonAncestor(self , root , o1 , o2 ):
        # write code here
        def dfs(root, o1, o2):
            if not root: return None
            # 只要遇到等于o1/o2的节点就返回
            if root.val == o1 or root.val == o2:
                return root
            left = dfs(root.left, o1, o2)
            right = dfs(root.right, o1, o2)
            if not left:
                return right
            if not right:
                return left
            return root
        return dfs(root, o1, o2).val