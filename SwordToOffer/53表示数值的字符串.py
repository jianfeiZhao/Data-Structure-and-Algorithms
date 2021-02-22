'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''
class Solution:
    '''
本题难点在于充分考虑各种可能出现的异常情况。
    '''
    def isNumeric(self, s):
        signe=0   #'e/E'符号标志位
        signd=0   #'.'符号标志位
        if not s:
            return False

        # 判断正负号
        if s[0]=='+' or s[0]=='-':
            s = s[1:]

        for i in range(len(s)):
            # 当前字符是'e'/'E'
            if s[i]=='e' or s[i]=='E':
                if signe==0:   #'e'/'E'只能出现一次
                    signe = 1
                elif signe==1:
                    return False
                if i==len(s)-1:   #'e'/'E'不能出现在最后
                    return False

            # 当前字符是'+'/'-'
            elif s[i]=='+' or s[i]=='-':
                if s[i-1]!='e' and s[i-1]!='E':   #只能紧跟着'e'/'E'出现
                    return False

            # 当前字符是'.'
            elif s[i]=='.':
                if signd==0:   #'.'只能出现一次
                    signd = 1
                elif signd==1:
                    return False
                if signe==1:   #'.'不能出现在'e'/'E'后
                    return False

            # 当前字符是除数字和'+'/'-'/'e'/'E'/'.'以外的其他字符
            elif s[i]>'9' or s[i]<'0':
                return False

        # 排除以上异常情况，返回True
        return True


s = Solution()
str_list = ["+100","5e2","-123","3.1416","-1E-16",\
            "12e","1a3.14","1.2.3","+-5","12e+4.3"]
for i in str_list:
    print(s.isNumeric(i))