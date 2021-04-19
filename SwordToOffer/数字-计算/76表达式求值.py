'''
请写一个整数计算器，支持加减乘三种运算和括号。
'''
priority = {'+': 0, '-': 0, '*': 1}
class Solution:
    def solve(self , s ):
        # write code here
        # 中缀表达式转为后缀表达式
        stack = []
        l = []
        tempnum = ''
        for i in s:
            if i <= '9' and i >= '0':
                tempnum += i
                continue
            else:
                if tempnum != '':
                    l.append(tempnum)
                    tempnum = ''
                if i == '(':
                    stack.append(i)
                elif i == ')':
                    temp = stack.pop()
                    while temp != '(':
                        l.append(temp)
                        temp = stack.pop()
                else:
                    if (not stack) or stack[-1] == '(' or (stack[-1] >= '0' and stack[-1] <= '9'):
                        stack.append(i)
                    else:
                        if priority[stack[-1]] < priority[i]:
                            stack.append(i)
                        else:
                            while stack and (stack[-1] in priority) and (priority[stack[-1]] >= priority[i]):
                                l.append(stack.pop())
                            stack.append(i)
        if tempnum != '':
            l.append(tempnum)
        while stack:
            l.append(stack.pop())
        #print(l)
        # 逆波兰法求后缀表达式的值
        for i in l:
            if i <= '9' and i >= '0':
                stack.append(i)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                temp = None
                if i == '*':
                    temp = num2*num1
                elif i == '-':
                    temp = num2-num1
                elif i == '+':
                    temp = num2+num1
                if temp:
                    stack.append(temp)
        return int(stack.pop())

s = Solution()
print(s.solve('(1+2)*3'))   # 9
print(s.solve('(1+2)*(3+4)+5'))   # 26