'''
用字符串模拟汇编语言中的循环左移（ROL）指令。
例如，字符序列S=”abcXYZdef”, 要求输出循环左移3位后的结果，即“XYZdefabc”。

YX = (X^T * Y^T)^T
'''
class Solution:
    def rolString(self, s, n):
        s1 = s[:n]
        s2 = s[n:]
        result = self.rev(self.rev(s1) + self.rev(s2))
        return result

    # 自定义字符串逆序函数
    def rev(self, s):
        l = ''
        for i in range(len(s)-1,-1,-1): #倒序循环
            l += s[i]
        return l

s = Solution()
string = 'abcXYZdef'
print(s.rolString(string, 3))