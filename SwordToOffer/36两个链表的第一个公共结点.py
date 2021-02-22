'''
输入两个链表，找出它们的第一个公共结点。
'''
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:
    def firstCommonNode(self, head1, head2):
        n1 = head1
        while n1:
            n2 = head2
            while n2:
                if n2 == n1:
                    return n1, n1.value
                else:
                    n2 = n2.next
            n1 = n1.next
        return None

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

# LinkedList1
n1.next = n2
n2.next = n4
n4.next = n5

# LinedList2
n2.next = n3
n3.next = n5

s = Solution()
print(s.firstCommonNode(n1, n2))    # n2
print(s.firstCommonNode(n4, n2))    # n5