'''
给定一个字符串，请编写一个函数判断该字符串是否回文。如果回文请返回true，否则返回false。

中心扩散
'''
class Solution:
    def judge(self , str ):
        # write code here
        def func(str, left, right):
            while left>=0 and right<len(str) and str[left]==str[right]:
                left -= 1
                right += 1
            if right - left < len(str)+1:
                return False
            else:
                return True
        mid = len(str)//2
        if len(str)%2 == 0:
            return func(str, mid-1, mid)
        if len(str)%2 == 1:
            return func(str, mid, mid)


# 2
while True:
    try:
        x = input()[1:-1].split(',')
        end = len(x)-1
        begin = 0
        while end>begin:
            if x[end]==x[begin]:
                end -= 1
                begin += 1
            else:
                print('false')
                break
        else:
            print('true')
    except:
        break