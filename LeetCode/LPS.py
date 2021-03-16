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

    def getLongestPalindrome(self, A, n):
        '''
思路1（动态规划，O(n^2)）从第一个字符往后遍历，把每个字符都当作中心去向两边扩散，
依次比较对称位置是否相等，当碰到左右边界停下。注意要分奇偶子串两种情况。
        '''
        def func(A, left, right):
            while left >=0 and right < n and A[left]==A[right]:
                left -= 1
                right += 1
            return right-left-1
        res = 0
        for i in range(n-1):
            res = max(res, func(A, i, i), func(A, i, i+1))
        return res

s = Solution()
ss = "bbdb"
print(s.LPS(ss))