'''
最长递增序列

前后比较
'''
class Solution:
    def LIS(self, arr):
        if not arr: return []
        else: res = [arr[0]]
        ls = []
        for i in range(1, len(arr)):
            if arr[i] > res[-1]:
                res.append(arr[i])
            else:
                print(res)
                ls.append(len(res))
                while res != [] and arr[i] < res[-1]:
                    res.pop()
                res.append(arr[i])
        print(res)
        ls.append(len(res))
        return max(ls)


s = Solution()
arr = [2,1,5,3,6,4,8,9,7]
print(s.LIS(arr))