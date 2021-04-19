'''
 给定一个数组arr，返回子数组的最大累加和
例如，arr = [1, -2, 3, 5, -2, 6, -1]，所有子数组中，[3, 5, -2, 6]可以累加出最大的和12，所以返回12.
题目保证没有全为负数的数据
[要求]
时间复杂度为O(n)，空间复杂度为O(1)
'''
class Solution:
    def maxsumofSubarray(self , arr ):
        # write code here
        if not arr: return
        if len(arr) == 1: return arr[0]
        m = 0  # 保存最大累加和
        for i in range(1, len(arr)):
            arr[i] = max(arr[i], arr[i-1]+arr[i])
            m = max(m, arr[i])
        return m