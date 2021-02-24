'''
LeetCode 322
different value of coins with unlimited number
find the minimum number of coins to change certain amount of money
'''
def coinChange(coins, amount):
  def dp(n):
    # base case
    if n == 0: return 0
    if n < 0: return -1

    # min problem, so init +inf
    res = float('INF')
    for coin in coins:
      subproblem = dp(n - coin)
      if subproblem == -1: continue   # no solution, skip   
      res = min(res, 1 + subproblem)
    return res if res != float('INF') else -1
  return dp(amount)


def coinChange2(coins, amount):
    memo = dict()    # memo
    def dp(n):
        if n in memo: return memo[n]
        # base case
        if n == 0: return 0
        if n < 0: return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n-coin)
            if subproblem == -1: continue
            res = min(res, 1+subproblem)

        memo[n] = res if res != float('INF') else -1
        return memo[n]
    return dp(amount)


def coinChange3(coins, amount):
    dp = [amount+1 for i in range(amount+1)]
    # base case
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if i-coin < 0: continue
            dp[i] = min(dp[i], 1+dp[i-coin])

    return dp[amount] if dp[amount] != amount+1 else -1


coins = [1,5,10]
amount = 47
#print(coinChange(coins, amount))
print(coinChange2(coins, amount))
print(coinChange3(coins, amount))