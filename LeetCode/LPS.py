'''
最长回文个数

状态: f[i][j] 表示 s 的第 i 个字符到第 j 个字符组成的子串中，最长的回文序列长度是多少。

转移方程: if s[i]==s[j], f[i][j] = f[i + 1][j - 1] + 2
        else f[i][j] = max(f[i + 1][j], f[i][j - 1])

遍历顺序: i 从最后一个字符开始往前遍历，j 从 i + 1 开始往后遍历，这样可以保证每个子问题都已经算好了。

初始化: f[i][i] = 1 单个字符的最长回文序列是 1

结果: f[0][n - 1]
'''
class Solution:
    def LPS(self, s):
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n-2, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

s = Solution()
ss = "bbbddb"
print(s.LPS(ss))