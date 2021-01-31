'''
求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
e.g 1~13中包含1的数字有1、10、11、12、13因此共出现6次.
'''
class Solution:
    '''
    对于一个数s利用循环移位和除10取余数的方法记录出现了几次1，
    再对从1到n的所有数遍历记录结果。算法复杂度高。
    '''
    def NumberOf1_1(self, n):
        count = 0
        while n > 0:
            s = n
            while s > 0:
                if s%10 == 1:
                    count +=1
                s = s//10    # 数s去掉最后一位
            n -= 1
        return count
    
    '''
    按位计算，记录每一位上会出现多少个1，累加返回结果。
    '''
    def NumberOf1_2(self, n):
        count = 0
        tmp = n
        base = 1   # 记录当前位数
        while tmp:
            last = tmp % 10   # 最后一位数
            tmp = tmp//10   # 右移一位
            count += tmp * base

            # 最后一位为1的情况比较特殊，单独讨论
            if last == 1:
                count += n % base + 1
            elif last > 1:
                count += base
            base *= 10
        return count

s = Solution()
n = 100
print(s.NumberOf1_1(n))
print(s.NumberOf1_2(n))