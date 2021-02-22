'''
统计一个数字在排序数组中出现的次数。
'''
class Solution:
    '''
先找到第一个相同数的位置，然后从这个位置开始直到出现不相同的数停止，输出计数结果。
    '''
    def count(self, ls, number):
        if ls == []: return 0
        for i in range(len(ls)):
            if ls[i] == number:
                break
        count = 0
        while ls[i] == number:
            count += 1
            i += 1
        return count

    '''
用二分查找k第一次出现的位置和最后一次出现的位置。
    '''
    def count2(self, ls, k):
        low = self.getLow(ls, k)
        high = self.getHigh(ls, k)
        return high-low+1

    def getLow(self, ls, k):
        start = 0
        end = len(ls)-1
        mid = (start+end)//2
        while start <= end:
            if data[mid] < k:
                start = mid+1
            else:            # data[mid]>=k
                end = mid-1
            mid = (end+start)//2
        return start
    
    def getHigh(self, ls, k):
        start = 0
        end = len(ls)-1
        mid = (start+end)//2
        while start <= end:
            if data[mid] <= k:
                start = mid+1
            else:            # data[mid]>k
                end = mid-1
            mid = (end+start)//2
        return end


data = [1,2,3,3,4,4,4,5,5,6,7,8,8]
s = Solution()
print(s.count(data, 4))
print(s.count(data, 9))
print(s.count2(data, 4))
print(s.count2(data, 9))