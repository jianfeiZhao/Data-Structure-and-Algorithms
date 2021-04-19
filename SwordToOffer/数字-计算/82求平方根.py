'''
实现函数 int sqrt(int x). 计算并返回x的平方根（向下取整） 
'''
class Solution:
    def sqrt(self , x):
        # write code here
        if x<0:
            return -1
        if x==0:
            return 0
        cur=1
        while True:
            pre=cur
            cur=(cur+x/cur)/2
            if abs(cur-pre)<1e-6:
                break
        return cur
    
    def sqrt(self , x):   # 牛顿迭代法
        if x == 0:
            return 0
        i, j = 1, x
        while i <= j:
            m = (i + j) // 2
            if m == x // m:
                return m
            if m > x // m:
                j = m - 1
            else:
                i = m + 1
        return i - 1