'''
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
'''
import time
class Solution:
    '''
用字典存储出现次数
    '''
    def findTwoNumber(self, ls):
        s = list(set(ls))
        result = []
        count = {}
        for i in s:
            count[i] = 0
        for j in ls:
            count[j] += 1
        for i in count:
            if count[i] == 1:
                result.append(i)
        return result
    
    '''
利用异或的思想来求解。一个数与它本身进行偶数次异或的结果为0。对数组做异或，最后剩下a^b，
再通过a, b两数最右边1的位置不同将两数分开。
    '''
    def findTwoNumber2(self, array):
        result = 0
        for obj in array:
            result ^= obj   # 异或运算，剩下的是a^b
        index = self.find_1_index(result)
        num1, num2 = 0, 0
        for obj in array:
            if self.is_bit_1(obj, index):
                num1 ^= obj
            else:
                num2 ^= obj
        return num1, num2

    # 找到最右边的1的位置，右移和与运算
    def find_1_index(self, digit):
        index = 0
        while not digit & 1:
            digit >>= 1
            index += 1
        return index
    
    # 判断右边第n位是否为1
    def is_bit_1(self, digit, n):
        digit >>= n
        return digit & 1     # 按位与运算

data = [i for i in range(1000000)] + [i for i in range(1000000)] + [1000000, 1000001]
s = Solution()
start = time.time()
print(s.findTwoNumber(data))
point1 = time.time()
print(point1-start, 's')

print(s.findTwoNumber2(data))
point2 = time.time()
print(point2-point1, 's')