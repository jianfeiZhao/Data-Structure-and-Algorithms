'''
给定一个数组arr，返回arr的最长无的重复子串的长度(无重复指的是所有数字都不相同)。
'''
class Solution:
    def maxLength(self, arr):
        left, right = 0, 0
        res = []
        for i in arr:
            if i in arr[left:right]:
                res.append(right-left)
                a = arr[left:right].index(i)+1
                left += a
            right += 1
        res.append(right-left)
        return max(res)

s = Solution()
arr = [2,2,3,4,3]
arr1 = [1,2,3,4,4,5,3,2,7]
print(s.maxLength(arr1))