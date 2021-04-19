'''
在一个字符串(0<=长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 
如果没有则返回 -1（需要区分大小写）.
'''
class Solution:
    '''
利用python内置函数list.count()和list.index()。
    '''
    def firstOnceChar(self, s):
        s = list(s)
        a = set(s)
        loc = len(s)    # record the location
        for i in a:
            if s.count(i) == 1 and s.index(i) < loc:  # find the first index
                loc = s.index(i)
        if loc == len(s):
            return -1
        return loc


string = 'fidAAIFnjjkIldacNJieakcIJfofjnfvmceiicjdiowesnjnd'
s = Solution()
print(s.firstOnceChar(string))