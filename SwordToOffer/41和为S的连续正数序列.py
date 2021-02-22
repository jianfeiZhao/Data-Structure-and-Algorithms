'''
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''
class Solution:
    def squenceSum(self, S):
        result = []
        seqSum = 0
        seq = []
        for i in range(1, S//2+2):
            seq.append(i)
            seqSum += i
            while seqSum > S:
                seqSum -= seq[0]
                seq = seq[1:]
            if seqSum == S:
                #print(seq)
                result.append(seq[::])
        return result

s = Solution()
print(s.squenceSum(15))
print(s.squenceSum(100))