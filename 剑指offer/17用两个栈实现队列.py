'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型

时间限制：1秒；空间限制：32768K

由于队列的特点是先进先出，而栈是先进后出，可以用两个栈串联来实现队列：栈1先进后出，栈1出栈栈2入栈，
栈2后进先出，从全局来看实现了先进先出的功能。
'''
import sys
sys.path.append(r"C:\Documents\GitHub\Data-Structure-and-Algorithms")
from Stack import Stack

class Solution:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, val):
        self.s1.push(val)

    def pop(self):
        for i in range(self.s1.size):
            self.s2.push(self.s1.pop())
        x = self.s2.pop()
        for i in range(self.s2.size):
            self.s1.push(self.s2.pop())
        return x

s = Solution()
arr = [1,2,3,4,5]
for i in range(len(arr)):
    s.push(arr[i])

print(s.pop())
print(s.pop())
print(s.pop())