'''
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
'''
class Solution:
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

data = [1,1,2,2,2,2,3,4,4,5]
s = Solution()
print(s.findTwoNumber(data))