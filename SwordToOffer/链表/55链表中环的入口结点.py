'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:
    '''
用一个list记录链表结点，空间复杂度大。
    '''
    def findCircleLs(self, head):
        if head == None:
            return None
        nodes = []
        while head.next:
            nodes.append(head)
            head = head.next
            if head in nodes:
                return head
        return None

    def hasCycle(self , head ):
        # write code here
        a, b = head, head
        while b and b.next:
            a, b = a.next, b.next.next
            if a == b:
                return True
        return False

    '''
第一步，找环中相汇点。分别用fast，slow指向链表头部，slow每次走一步，fast每次走二步，直到slow==fast找到在环中的相汇点。
第二步，找环的入口。当slow==fast时，让其中一个指针指向链表头部，另一个位置不变，fast和slow每次都走一步直到再次slow==fast，此时指向的是环的入口。
    '''
    def findCircleLs2(self, head):
        # 找环中相汇点
        a, b = head, head
        while b and b.next:
            a, b = a.next, b.next.next
            if a == b:
                # 找环的入口
                b = head
                while b != a:
                    b = b.next
                    a = a.next
                return a


s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(s.findCircleLs(node1))
print(s.findCircleLs2(node1))