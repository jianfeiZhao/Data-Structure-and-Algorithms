'''
输入两个单调递增的链表，输出两个链表合成后的链表，合成后的链表也满足单调递增。

时间限制：1秒；空间限制：32768K；本题知识点：链表
'''

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
 
class Solution:
    def mergeTwoList(self, head1, head2):
        p = Node(1)
        new = p
        while head1!=None and head2!=None:
            if head1.val < head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
            p = p.next   #记得更新p
        if head1!=None: #注意不要写成while
            p.next = head1
        if head2!=None:
            p.next = head2
        return new.next

# list1
a1 = Node(1)
a2 = Node(4)
a3 = Node(5)
a4 = Node(9)
a1.next = a2
a2.next = a3
a3.next = a4

# list2
b1 = Node(2)
b2 = Node(5)
b3 = Node(6)
b4 = Node(10)
b1.next = b2
b2.next = b3
b3.next = b4

# test
for head in (a1,b1):
    print('List:')
    while head!=None:
        print(head.val,'-->')
        head = head.next

s = Solution()
head = s.mergeTwoList(a1, b1)
print('After Merge:')
while head!=None:
    print(head.val,'-->')
    head = head.next
