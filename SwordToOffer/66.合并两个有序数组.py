'''
给出两个有序的整数数组 A 和 B，请将数组 B 合并到数组 A 中，变成一个有序的数组
注意：
可以假设 A 数组有足够的空间存放 B 数组的元素， A 和 B 中初始的元素数目分别为 m 和 n 
'''
class Solution:
    def merge(self , A, m, B, n):
        # write code here
        if not A or not B: return A+B
        while m > 0 and n > 0:
            if A[m-1] >= B[n-1]:
                A[m+n-1] = A[m-1]
                m -= 1
            else:
                A[m+n-1] = B[n-1]
                n-=1
        if n > 0: A[:n] = B[:n]
        return A