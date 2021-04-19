'''
如果数组中元素大于等于左边最大，小于等于左边最小，则置1，否则置0.
'''
#nums = [7,4,5,8,9,17,15,14,18,19]
nums = eval(input())
res = []
maxNum = nums[0]
for i in range(len(nums)):
    if nums[i] >= maxNum:
        maxNum = nums[i]
        res.append(1)
    else:
        res.append(0)

minNum = nums[len(nums)-1]
for i in range(len(nums)-1, -1, -1):
    if nums[i] <= minNum:
        minNum = nums[i]
    else:
        if res[i] == 1:
            res[i] = 0
print(res)