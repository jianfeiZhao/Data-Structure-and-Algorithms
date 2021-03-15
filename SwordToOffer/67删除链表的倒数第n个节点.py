'''
 给定一个链表，删除链表的倒数第n个节点并返回链表的头指针
例如，
 给出的链表为:1->2->3->4->5, n= 2.
 删除了链表的倒数第n个节点之后,链表变为1->2->3->5.
备注：
题目保证n一定是有效的，请给出时间复杂度为 O(n) 的算法
'''
class Solution:
    def removeNthFromEnd(self , head , n ):
        # 快慢指针
        p, q = head, head
        while n>0:
            if p:
                p = p.next
            else:
                return None
            n -= 1
        if not p: return head.next
        while p:
            p = p.next
            pre = q
            q = q.next
            if not p:
                pre.next = q.next
        return head