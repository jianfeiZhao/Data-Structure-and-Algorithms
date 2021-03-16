'''
分别按照二叉树先序，中序和后序打印所有的节点。
'''
class Solution:
    def threeOrders(self , root ):
        # write code here
        pre_order, in_order, post_order = [], [], []
        def find(root):
            if not root: return None
            pre_order.append(root.val)  # 先序：根左右
            find(root.left)
            in_order.append(root.val)   # 中序：左根右
            find(root.right)
            post_order.append(root.val) # 后序：左右根
        find(root)
        return [pre_order, in_order, post_order]