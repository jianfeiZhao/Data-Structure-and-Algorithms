'''
给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
class Solution:
    def twoSum(self, nums, target):
        num = nums.copy()
        n = 0
        while len(num):
            i = num.pop(0)
            n += 1
            if target-i in num:
                return [nums.index(i),num.index(target-i)+n]
    
    def twoSum1(self, nums, target):
        if len(nums)  == 0:
            return None
        lookup = {}
        for i in range(len(nums)-1):
            lookup[nums[i]] = i
            if target - nums[i] in lookup.keys():
                return [i, lookup[target-nums[i]]]

nums = [4,2,6,13,2,8]
target = 15
s = Solution()
print(s.twoSum(nums, target))
print(s.twoSum1(nums, target))
