'''
 给出一个有n个元素的数组S，S中是否有元素a,b,c满足a+b+c=0？找出数组S中所有满足条件的三元组。
注意：
    三元组（a、b、c）中的元素必须按非降序排列。（即a≤b≤c）
    解集中不能包含重复的三元组。 

例如，给定的数组 S = {-10 0 10 20 -10 -40}, 解集为(-10, 0, 10) (-10, -10, 20)
'''
class Solution:
    def threeSum(self , num ):
        # write code here
        num.sort()
        res = []
        for cur in range(len(num)-2):
            if num[cur] > 0:
                break
            if cur > 0 and num[cur] == num[cur-1]:
                continue
            left = cur + 1
            right = len(num) -1
            while left < right:
                sums = num[cur] + num[left] + num[right]
                if sums < 0:
                    left += 1
                elif sums > 0:
                    right -= 1
                else:
                    res.append([num[cur], num[left], num[right]])
                    left += 1
                    right -= 1
                    while left < right and num[left] == num[left-1]:
                        left += 1
                    while left < right and num[right] == num[right+1]:
                        right -= 1
        return res