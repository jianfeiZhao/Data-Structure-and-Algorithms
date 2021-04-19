'''
给定一个 n * m 的矩阵 a，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，
路径上所有的数字累加起来就是路径和，输出所有的路径中最小的路径和。
'''
class Solution:
    def minPathSum(self , matrix ):
        # write code here
        r = len(matrix)
        c = len(matrix[0])
        dp = [0] * c

        dp[0] = matrix[0][0]

        for i in range(1,c):
            dp[i] = dp[i - 1] + matrix[0][i]

        for i in range(1,r):
            dp[0] += matrix[i][0]

            for j in range(1,c):
                dp[j] = min(dp[j -1],dp[j]) + matrix[i][j]

        return dp[-1]