'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。

n<=39

时间限制：1秒；空间限制：32768K
'''

def Fibonacci1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return Fibonacci1(n-1) + Fibonacci1(n-2)
    
#print(Fibonacci1(39))   # 不满足时间限制

def Fibonacci2(n):
    i=0        # n = 0
    j=1        # n = 1
    while n>0:   
        # i, j各往前进一步
        j += i
        i = j-i
        n -= 1
    return i

assert Fibonacci2(2) == 1
assert Fibonacci2(3) == 2
assert Fibonacci2(5) == 5
assert Fibonacci2(6) == 8
print('test pass!')
print(Fibonacci2(39))