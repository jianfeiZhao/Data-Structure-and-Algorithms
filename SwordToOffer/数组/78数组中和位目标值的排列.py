'''
给出一组候选数 C 和一个目标数 T，找出候选数中起来和等于 T 的所有组合。
C 中的每个数字在一个组合中只能使用一次。
注意：
    题目中所有的数字（包括目标数 T ）都是正整数
    组合中的数字 (a1,a2,…,aka_1, a_2, … , a_ka1​,a2​,…,ak​) 要按非递增排序 (a1≤a2≤…≤aka_1 \leq a_2 \leq … \leq a_ka1​≤a2​≤…≤ak​).
    结果中不能包含重复的组合
    组合之间的排序按照索引从小到大依次比较，小的排在前面，如果索引相同的情况下数值相同，则比较下一个索引。 
'''
class Solution:
    def combinationSum2(self , num , target ):
        # write code here
        res = []
        def backtrack(num, path, target, start):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(num)):
                if num[i] > target:
                    break
                if i > start and num[i] == num[i - 1]:
                    continue
                backtrack(num, path + [num[i]], target - num[i], i + 1)
        num.sort()
        backtrack(num, [], target, 0)
        return res