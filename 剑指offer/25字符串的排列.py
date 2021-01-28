'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。 
结果请按字母顺序输出。 

递归的思路，把问题分解为：循环字符串，假设每次循环元素为a，将字符串当前元素a固定在第一个位置，
再与除了a的剩余元素求排列的结果拼接求和。再利用集合set进行去重，sorted()函数排序。
'''
class Solution:
    def permutation(self, ss):
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]
        ls = []
        # traverse string, every time put the fixed element to the first position
        for i in range(len(ss)):
            for j in self.permutation(ss[:i]+ss[i+1:]):
                ls.append(ss[i] + j)
        # set(), sorted()
        return sorted(list(set(ls)))

s = Solution()
str1 = 'abc'
#str2 = 'aab'
print(s.permutation(str1))
#print(s.permutation(str2))