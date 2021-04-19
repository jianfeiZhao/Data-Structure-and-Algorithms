'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
class Solution:
    def findNumber(self, ls):
        length = len(ls)
        p = length//2
        if length == 0:
            return 0
        if length == 1:
            return ls[0]
        count = {}
        for i in range(length):
            if ls[i] in count.keys():
                count[ls[i]] += 1
                if count[ls[i]] > p:
                    return ls[i]
            else:
                count[ls[i]] = 1
        return 0

s = Solution()
ls1 = [1,2,3,2,2,2,5,4,2]
ls2 = [1,2,3,5,4,2]
print(s.findNumber(ls1))
print(s.findNumber(ls2))