'''
输入一组不重复的数字，返回它们的全排列

在递归之前做出选择，在递归之后撤销刚才的选择，就能正确得到每个节点的选择列表和路径。
回溯算法，不像动态规划存在重叠子问题可以优化，回溯算法就是纯暴力穷举，复杂度一般都很高。
'''
import copy

class Solution:
    res = []
    def permute(self, nums):  
        track = []
        self.backtrack(nums, track)
        return self.res

    def backtrack(self, nums, track):
        # trigger end condition
        if len(track) == len(nums):
            self.res.append(copy.deepcopy(track))
            return

        for i in range(len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            # next choice
            self.backtrack(nums, track)
            # go back to make another choice, remove current choice
            track.pop()


s = Solution()
data = [1,2,3]
print(s.permute(data))