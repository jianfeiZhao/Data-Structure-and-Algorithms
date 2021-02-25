'''
输入一组不重复的数字，返回它们的全排列

在递归之前做出选择，在递归之后撤销刚才的选择，就能正确得到每个节点的选择列表和路径。
'''
res = []
def permute(nums):  
    track = []
    backtrack(nums, track)
    return res

def backtrack(nums, track):
    # trigger end condition
    if len(track) == len(nums):
        res.append(track)
        return

    for i in range(len(nums)):
        if nums[i] in track:
            continue
        track.append(nums[i])
        # next choice
        backtrack(nums, track)
        # go back to make another choice, remove current choice
        track.pop()


data = [1,2,3,4]
print(permute(data))