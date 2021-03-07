'''
给定两个字符串str1和str2,输出两个字符串的最长公共子串
O(m*n)
'''
class Solution:
    def LCS(self, str1, str2):
        # 连续
        m = len(str1)
        n = len(str2)
        # base case
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        maxLen = 0
        end = -1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                if dp[i][j] > maxLen:
                    maxLen = dp[i][j]
                    end = j-1
        if end == -1: return -1
        else: res = str2[end-maxLen+1:end+1]
        return res


    def LCS2(self, str1,  str2):
        # 不连续
        m = len(str1)
        n = len(str2)
        res = ''
        # base case
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res += str1[i-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return res


str1 = "1AB234CD"
str2 = "12345EF"
s = Solution()
print(s.LCS(str1, str2))
print(s.LCS2(str1, str2))