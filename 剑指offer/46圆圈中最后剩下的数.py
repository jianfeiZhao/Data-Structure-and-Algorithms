'''
首先,让小朋友们围成一个大圈。然后,随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
从他的下一个小朋友开始,继续0...m-1报数,直到剩下最后一个小朋友,可以不用表演,并且拿到名贵的礼品。
请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
'''
class Solution:
    def lastNumber(self, n, m):
        if not m or not n:
            return -1
        ls = [i for i in range(n)]   # init list of kids
        i = -1   # loop
        loc = -1   # record the location
        while len(ls) > 1:
            i += 1
            loc += 1
            if loc >= len(ls):   # when loc = len(ls)+1, zero out
                loc -= len(ls)   # loc = 0
            if i == m-1:
                ls.pop(loc)
                i = 0   # next loop
        return ls[0]

s = Solution()
n = 10         # number od kids
print(s.lastNumber(n, 15))

'''
result = []
for i in range(2, 100):
    result.append(s.lastNumber(n, i))
for i in range(n):
    print(i, result.count(i))
'''