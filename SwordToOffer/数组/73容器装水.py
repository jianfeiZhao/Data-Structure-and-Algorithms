'''
给定一个整形数组arr，已知其中所有的值都是非负的，将这个数组看作一个容器，请返回容器能装多少水。 
'''
class Solution:
    def maxWater(self , arr ):
        # write code here
        if arr is None or len(arr)<=2:
            return 0
        get_water = 0
        tmp=arr[0]
        sum_tmp=0
        maxh=max(arr)
        idxh=arr.index(maxh)
        for i in arr[0:idxh+1]:
            if i>=tmp:
                tmp=i
                get_water+=sum_tmp
                sum_tmp=0
            else:
                sum_tmp+=tmp-i
        tmp=arr[-1]
        sum_tmp=0
        arr_new=arr[idxh:]
        for i in arr[::-1]:
            if i>=tmp:
                tmp=i
                get_water+=sum_tmp
                sum_tmp=0
            else:
                sum_tmp+=tmp-i
        return get_water

s = Solution()
arr = [2,4,2,3,1,2,5,2]
print(s.maxWater(arr))