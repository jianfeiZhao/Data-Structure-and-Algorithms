'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，
输出两个数的乘积最小的。

如果存在两个数和为S，那么这两数差值越大（即离得越远）则乘积越小。
利用for循环，外循环正序，内循环倒序，则第一次找到的结果即为乘积最小的结果。
'''
class Solution:
    def printTwoSum(self, arr, S):
        result = []
        for i in range(len(arr)):
            for j in range(len(arr)-1, -1, -1):   # 倒序
                if arr[i] + arr[j] == S and arr[i] != arr[j]:
                    result.append(arr[i])
                    result.append(arr[j])
                    return result
        return result

data = [1,2,5,9,12,14,20,23]
s = Solution()
print(s.printTwoSum(data, 14))
print(s.printTwoSum(data, 26))
print(s.printTwoSum(data, 36))