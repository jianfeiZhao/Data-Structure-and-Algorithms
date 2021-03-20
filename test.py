'''
def func(A, left, right):
    while left >= 0 and right < n:
        while A[left] == A[right] or A[left] == '*' or A[right] == '*':
            left -= 1
            right += 1
    return right-left-1
res = 0
A = input()
n = len(A)
for i in range(n-1):
    res = max(res, func(A, i, i), func(A, i, i+1))
print(res)
'''
def LPS(s):
    n = len(s)
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n-2, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j] or s[i] == '*' or s[j] == '*':
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

A = input()
print(LPS(A))