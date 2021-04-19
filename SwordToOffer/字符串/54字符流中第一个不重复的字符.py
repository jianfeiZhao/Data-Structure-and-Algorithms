'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

输出描述:
如果不存在出现一次的字符，返回#字符。
'''
class Solution:
    '''
用一个足够大的数组来记录对应ascii码值的字符出现的次数，再判断字符流中第一个不重复的字符。ord()
    '''
    def __init__(self):
        self.s = [0]*256   #ascii码表记录出现次数
        self.l = ''   #记录输入字符流

    def firstAppearOnce(self):
        for i in self.l:
            if self.s[ord(i)] == 1:   #仅出现一次
                return i
        return '#'

    def insert(self, char):
        self.l = self.l + char
        self.s[ord(char)] += 1


s = Solution()
for i in 'google':
    s.insert(i)
    print(s.firstAppearOnce())