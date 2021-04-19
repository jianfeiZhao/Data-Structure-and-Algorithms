'''
给出一个转动过的有序数组，你事先不知道该数组转动了多少(例如,0 1 2 4 5 6 7可能变为4 5 6 7 0 1 2).
在数组中搜索给出的目标值，如果能在数组中找到，返回它的索引，否则返回-1。
假设数组中不存在重复项。

二分法查找
'''
class Solution:
    def search(self , A , target ):
        # write code here
        n = len(A)
        l, r = 0, n-1
        while l <= r:
            mid = l + (r-l) // 2
            if A[mid] == target:
                return mid
            if A[mid] < A[r]:
                if A[mid] < target <= A[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif A[l] < A[mid]:
                if A[l] <= target < A[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                l += 1
        return -1