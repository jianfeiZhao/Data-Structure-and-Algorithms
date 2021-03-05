# LeetCode 509
# from top to bottom(slow)
def fib1(n):
  dp = [0 for i in range(n+1)]    # memo
  if n in (1,2): return 1
  if dp[n] != 0: return dp[n]
  return fib1(n-1) + fib1(n-2)


# from bottom to top
def fib2(n):
  if n<1: return 0
  if n in (1,2): return 1
  dp = [0 for i in range(n+1)]    # memo
  dp[1], dp[2] = 1, 1
  for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
  return dp[n]


# space compression
def fib3(n):
  if n<1: return 0
  if n in (1,2): return 1
  cur, pre = 1, 1   # only need two vars for storage
  for i in range(3, n+1):
    sum = cur + pre
    pre = cur
    cur = sum
  return sum


print(fib1(20))
print(fib2(40))
print(fib3(40))