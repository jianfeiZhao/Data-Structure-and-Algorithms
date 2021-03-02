'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

任意两个丑数相乘的结果还是丑数，任意大于1的丑数可以由一个丑数乘以2/3/5得到.
可以用三个索引值i1/i2/i3记录当前的丑数可由2/3/5哪个数计算出。
每次循环只需要计算三次乘法的结果比较并记录最小值，然后更新索引值i，这样就能按从小到大的顺序得到丑数数组。
'''
class Solution:
    def uglyNumber(self, N):
        if N == 0: return 0
        ls = [1]   # ugly list
        i1, i2, i3 = 0, 0, 0
        while len(ls) < N:
            num1 = ls[i1] * 2
            num2 = ls[i2] * 3
            num3 = ls[i3] * 5
            num = min(num1, num2, num3)
            #print(num)
            ls.append(num)
            if num == num1:
                i1 += 1
            if num == num2:
                i2 += 1
            if num == num3:
                i3 += 1
        return ls[-1]

s = Solution()
print(s.uglyNumber(20))