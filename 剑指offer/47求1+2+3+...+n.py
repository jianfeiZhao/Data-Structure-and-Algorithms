'''
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

利用逻辑运算的短路特性，作为递归的终止条件。
(表达式1）&&(表达式2) 如果表达式1为假，则表达式2不会进行运算，即表达式2“被短路”
(表达式1）||(表达式2) 如果表达式1为真，则表达式2不会进行运算，即表达式2“被短路”

python中逻辑运算符的用法：a and b，a为False返回a，a为True就返回b.
'''
class Solution:
    def nSum(self, n):
        result = n
        a = n and self.nSum(n-1)
        #print(a)
        result += a
        return result

s = Solution()
print(s.nSum(10))