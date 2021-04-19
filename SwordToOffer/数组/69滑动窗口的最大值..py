'''
窗口从数组首部滑到尾部，记录窗口内的最大值
'''
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size==0: return []
        l, r =0, size-1
        res = []
        for i in range(len(num)-size+1):
            res.append(max(num[l:r+1]))
            l += 1
            r += 1
        return res