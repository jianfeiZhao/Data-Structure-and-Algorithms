'''
给定两个字符串str1和str2，再给定三个整数ic，dc和rc，分别代表插入、删除和替换一个字符的代价，
请输出将str1编辑成str2的最小代价。

1.动态规划：dp[i][j]表示word1的前i个字符编辑成word2的前j个字符需要的最小操作数
2.初始状态：dp[i][0] = i，i次删除；dp[0][i] = i，i次插入
3.过渡公式：
    当i字符等于j字符时：dp[i][j] = dp[i-1][j-1]，不需要额外操作
    当i字符不等于j字符时：dp[i][j] = Math.min(insert, delete, replace)
    int insert = dp[i][j-1] + 1; i个编辑成j-1个字符，再插入一个j
    int delete = dp[i-1][j] + 1; i-1个编辑成j个字母，再删除一个i
    int replace = dp[i-1][j-1] + 1; i-1个编辑成j-1个字母，再将i替换成j 
'''
class Solution:
    def minEditCost(self , str1 , str2 , ic , dc , rc ):
        # write code here
        len1, len2 = len(str1) + 1, len(str2) + 1
        dp = [0 for i in range(len2)]
        for i in range(1, len2):
            dp[i] = i * ic
        for i in range(1, len1):
            prev = dp[0]
            dp[0] = i * dc
            for j in range(1, len2):
                tmp = dp[j]
                if str1[i - 1] == str2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j - 1] + ic, tmp + dc, prev + rc)
                prev = tmp
        return dp[j]