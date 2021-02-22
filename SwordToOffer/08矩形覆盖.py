'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
总共有多少种方法？

时间限制：1秒；空间限制：32768K

经过分析，这还是一个斐波那契数列。
当n=1时，覆盖方法f(1) 有1种； 
当n=2时，覆盖方法f(2) 有2种；
当n>2时，覆盖方法有f(n)=f(n-1)+f(n-2)种，是在第n-1种方案基础上竖着覆盖一个和在第n-2种方案基础上
横着覆盖两个的结果和，其他情况都被包含在第n-1和第n-2种方案里了。
'''
class Solution:
    def rectCover(self, n):
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        i = 1
        j = 2
        while n > 2:
            j += i
            i = j - i
            n -= 1
        return j

# test
s = Solution()
assert s.rectCover(2) == 2
assert s.rectCover(3) == 3
assert s.rectCover(4) == 5
assert s.rectCover(6) == 13
print('test pass!')



