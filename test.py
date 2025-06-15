'''
inp = input().split('\n')
for line in inp:
    n, m = line.split(' ')
    n, m = int(n), int(m)
    for i in range(m):
        res = n + round(n**0.5, 2)
    print(round(res,2))
'''
class Solution:
    def findValue(self, nums):
        if not nums: return None
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

arr1 = [0,1,2,4]
arr2 = [0,1,2]
s = Solution()
print(s.findValue(arr1))   # 3
print(s.findValue(arr2))   # 3