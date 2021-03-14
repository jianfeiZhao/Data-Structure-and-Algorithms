'''

'''
class Solution:
    def jumpFloor(self, number):  # k=2
        # write code here
        ls = [0 for i in range(3)]
        ls[0] = 1
        ls[1] = 1
        for i in range(2, number+1):
            ls[i%2] += ls[(i-1)%2]
        return ls[number%2]


def climbKSteps(n, k):
  ls = [0 for i in range(n+1)]
  ls[0] = 1
  ls[1] = 1
  for i in range(2, n+1):
    for j in range(1, k+1):
      if i-j < 0:
        continue
      ls[i] += ls[i-j]
  return ls[n]

# reduce space complexity
def climbKSteps1(n, k):
  ls = [0 for i in range(k+1)]
  ls[0] = 1
  ls[1] = 1
  for i in range(2, n+1):
    for j in range(1, k):
      if i-j < 0:
        continue
      ls[i%k] += ls[(i-j)%k]
  return ls[n%k]


# not allowed to step on stairs in s
def climbKSteps2(n, k, s):
  ls = [0 for i in range(k+1)]
  ls[0] = 1
  ls[1] = 1
  for i in range(2, n+1):
    for j in range(1, k):
      if i-j < 0:
        continue
      if s[i-1] == 1:
        ls[i%k] = 0
      ls[i%k] += ls[(i-j)%k]
  return ls[n%k]

n = 8
k = 4
s = [0 for i in range(8)]
s[1] = 1
s[3] = 1
s[4] = 1
s[6] = 1
climbKSteps2(n, k, s)


# climb stairs with diff price
# find the min cost to step n stairs
def climbKSteps3(n, k, p):
  ls = [0 for i in range(n+1)]
  # base cases
  ls[0] = 0
  ls[1] = p[1]
  for i in range(2, n+1):
    for j in range(1, k):
      if i-j < 0:
        continue
      if ls[i-j] > ls[i-j-1]:
        min = ls[i-j-1]
      else: min = ls[i-j]
    ls[i] = p[i] + min
  return ls[n]

p = [0,3,2,4,5,1,3,2,3]
climbKSteps3(8, 3, p)