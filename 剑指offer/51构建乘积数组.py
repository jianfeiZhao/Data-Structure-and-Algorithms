'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。
'''
class Solution:
    '''
两次循环实现除自身外的累乘，时间复杂度较大。
    '''
    def createArray(self, arr):
        arrB = [1 for i in range(len(arr))]
        for i in range(len(arr)):
            arrA = arr.copy()
            del arrA[i]
            for j in arrA:
                arrB[i] *= j
        return arrB
    
    '''
矩阵被分为上三角矩阵和下三角矩阵，分别求得连乘值，最后上三角连乘值乘以对应下三角连乘值即可。
    '''
    def createArray2(self, arr):
        L1 = [1]    #下三角连乘值，长度n，初始1
        L2 = [1]    #上三角连乘值，长度n，倒序，初始1
        L = []      #结果数组，长度n
        for i in range(1,len(arr)):
            L1.append(L1[i-1]*arr[i-1])
            L2.append(L2[i-1]*arr[-i])
        for i in range(len(arr)):
            L.append(L1[i]*L2[-(i+1)])   # 间隔一个i
        return L

s = Solution()
arr = [1,2,3]
print(s.createArray(arr))      # [6,3,2]
print(s.createArray2(arr))      # [6,3,2]