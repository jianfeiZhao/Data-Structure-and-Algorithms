'''
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


coins = [1,5,10]
amount = 27
print(coinChange(coins, amount))