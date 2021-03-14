'''
给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()", "[()]"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。
'''
class Solution:
    # 字符串替换
    def isValid(self , s ):
        # write code here
        if not s: return False
        flag = True
        while flag:
            n = len(s)
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            if not s: return True    # 括号已全部移除
            if n == len(s):
                flag = False
        return False

    # push and pop in stack
    def isValid2(self , s ):
        # write code here
        if not s: return False
        stack = []
        for i in s:
            if i in ('(','[','{'):
                stack.append(i)      # push
            if i in (')',']','}'):
                if not stack: return False
                a = stack.pop()      # pop
                if i == ')' and a == '(':
                    continue
                elif i == ']' and a == '[':
                    continue
                elif i == '}' and a == '{':
                    continue
                else:
                    stack.append(a)
        if not stack: return True
        else: return False