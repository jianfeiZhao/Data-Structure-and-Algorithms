'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

时间限制：1秒；空间限制：32768K；本题知识点： 数组
'''
class Solution:
    def reOrderArray(self, arr):
        odd,even=[],[]
        for i in arr:
            odd.append(i) if i%2==1 else even.append(i)
        return odd+even
    
    def reOrderArray1(self, array):
        return sorted(array,key=lambda x:x%2,reverse=True)

# test
arr = [6,4,6,3,7,8,9,12,1]
s = Solution()
print(s.reOrderArray(arr))
print(s.reOrderArray1(arr))