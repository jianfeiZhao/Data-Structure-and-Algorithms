'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个升序数组的一个旋转，
输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

时间限制：1秒；空间限制：32768K；本题知识点：查找
'''
class Solution:
    # O(N) 逐个遍历
    def S1(self, sortedArray):
        if len(sortedArray) == 0:
            return 0
        if len(sortedArray) == 1:
            return sortedArray[0]        
        for i in range(len(sortedArray)-1):
            if sortedArray[i+1] < sortedArray[i]:
                return sortedArray[i+1]
        return sortedArray[i+1]
    
    # 二分查找O(logN)
    def S2(self, arr):
        left = 0                # left index
        right = len(arr) - 1      # right index
        if len(arr) == 0:
            return 0
        while (right-left) != 1:
            mid = int((left + right)/2)
            if arr[mid] == arr[left] == arr[right]:
                return min(arr[left:right+1])
            if arr[left] <= arr[mid]:
                left = mid
            else:
                right = mid
       # mid = right
        return arr[right]


arr1 = [4,5,6,7,8,9,2,2,2,2,3]
arr2 = [1,0,1,1,1,1,1]

s = Solution()
assert s.S2(arr1) == 2
assert s.S2(arr2) == 0
print('test pass!')
            