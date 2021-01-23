'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。

如果一个序列是合法的BST的后序序列，那么满足以下条件：
1、最后一个元素是根节点root；
2、root前面的序列可以分为两段：前一段序列是左子树，值都小于root值；后一段序列是右子树，值都大于root值；
3、这两段序列也都是合法的BST的后序序列。
'''
class Solution:
    def VerifyBST(self, sequence):
        if sequence == None or sequence == []:
            return False
        root = sequence[-1]
        size = len(sequence)
        # find left subtree
        for i in range(size):
            if sequence[i] > root:
                break

        # verify right subtree
        for j in range(i, size-1):
            if sequence[j] <= root:
                return False

        # whether left subtree is BST
        left = True
        if i>0:
            left = self.VerifyBST(sequence[0:i])
        
        # whether right subtree is BST
        right = True
        if i<size-1:
            right = self.VerifyBST(sequence[i:-1])

        return left and right

postorder = [2,7,5,14,11,10]
badorder = [10,5,2,7,11,14]
s = Solution()        
print(s.VerifyBST(postorder))
print(s.VerifyBST(badorder))