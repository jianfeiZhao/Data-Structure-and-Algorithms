'''
给你一个 N×N 的棋盘，让你放置 N 个皇后，使得它们不能互相攻击。
PS：皇后可以攻击同一行、同一列、左上左下右上右下四个方向的任意单位。

这个问题本质上跟全排列问题差不多，决策树的每一层表示棋盘上的每一行；
每个节点可以做出的选择是，在该行的任意一列放置一个皇后。

这个问题的复杂度非常高，虽然有 isValid 函数剪枝，但是最坏时间复杂度仍然是 O(N^(N+1))，而且无法优化.
有的时候，我们并不想得到所有合法的答案，只想要一个答案.
'''
import copy

class Solution:
    res = []
    def nQueens(self, n):
        # '.' 表示空，'Q' 表示皇后，初始化空棋盘
        board = [['.' for i in range(n)] for j in range(n)]
        self.backtrack(board, 0)
        return self.res

    def backtrack(self, board, row):
        ########### finish
        if row == len(board):
            board = [''.join(board[i]) for i in range(len(board))]
            self.res.append(copy.deepcopy(board))
            return True
        
        n = len(board[row])
        for col in range(n):
            if not self.isValid(board, row, col):
                continue
            ########### choose
            board[row][col] = 'Q'
            ############ next decision
            #if self.backtrack(board, row+1):   # 只返回一个答案
                #return True
            self.backtrack(board, row+1)   # 返回所有答案
            ############# remove choice
            board[row][col] = '.'
        return False

    def isValid(self, board, row, col):
        n = len(board)
        # check collisions on col
        for i in range(n):
            if board[i][col] == 'Q':
                return False

        # check collisions on right up
        for i in range(row-1, -1, -1):
            if col+row-i < n and board[i][col+row-i] == 'Q':
                return False
        
        # check collisions on left up
        for i in range(row-1, -1, -1):
            if col-row+i >= 0 and board[i][col-row+i] == 'Q':
                return False
        return True


s = Solution()
print(s.nQueens(4))