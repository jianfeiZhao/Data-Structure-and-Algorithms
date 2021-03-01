'''
给你一个 N×N 的棋盘，让你放置 N 个皇后，使得它们不能互相攻击。
PS：皇后可以攻击同一行、同一列、左上左下右上右下四个方向的任意单位。

这个问题本质上跟全排列问题差不多，决策树的每一层表示棋盘上的每一行；
每个节点可以做出的选择是，在该行的任意一列放置一个皇后。
'''
class Solution:
    res = []
    def nQueens(self, n):
        # '.' 表示空，'Q' 表示皇后，初始化空棋盘
        board = [['.' for i in range(n)] for j in range(n)]
        self.backtrack(board, 0)
        return self.res

    def backtrack(self, board, row):
        # finish
        if row == len(board):
            board = [''.join(board[i]) for i in range(len(board))]
            #print(board)
            self.res.append(board)
            return
        
        n = len(board[row])
        for col in range(n):
            if not self.isValid(board, row, col):
                continue
            # choose
            board[row][col] = 'Q'
            # next decision
            self.backtrack(board, row+1)
            # remove choice
            board[row][col] = '.'

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