'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
输入一个链表，输出该链表中倒数第k个结点。返回的是Node，而不是Node的Value。注意处理k超出范围的异常情况。
输入一个链表，反转链表后，输出新链表的表头。

时间限制：1秒；空间限制：32768K；本题知识点：链表
'''
class node:
    def __init__(self, x):
        self.val = x
        self.next = None
 
class Solution:
    def printListFromTailToHead1(self, node):
        l = []
        while node:
            l.insert(0, node.val)    # 头插法，得到链表的倒序list
            node = node.next
        return l
 
    def printListFromTailToHead2(self, node):
        l = []
        while node:
            l.append(node.val)   # 尾插法，得到链表的正序list
            node = node.next
        return l[::-1]   # 翻转输出结果

    def FindKthToTail1(self, head, k):
        l=[]                # use extra space
        while head:
            l.append(head)
            head = head.next
        if len(l)<k or k<=0:      # k out of range
            return
        return l[-k]
    
    def FindKthToTail2(self, head, k):
        p,pre=head,head
        i=0
        while pre!=None:
            i+=1       # use i to count the length of the linkls
            if i>k:      # when the length reach k, use p to record the Kth to tail
                p=p.next
            pre=pre.next
        if k>i or k<=0:       # k out of range
            return 
        return p
    
    def ReverseLinkls(self, head):
        if head==None or head.next==None:
            return head
        pre = None       # current
        cur = head       # previous
        while cur:
            tmp = cur.next    
            cur.next = pre    # current node points to previous node

            pre = cur     # cur node become pre node
            cur = tmp     # next node becomr cur node
        return pre

# build linked list
node1 = node([1,2,3])
node2 = node([4,5,6])
node3 = node([7,8])
node4 = node([9])
node1.next = node2
node2.next = node3
node3.next = node4

# test
s = Solution()
print(s.printListFromTailToHead1(node1))
print(s.printListFromTailToHead2(node1))
print('-------------------------------')
print(s.FindKthToTail1(node1, 6))
print(s.FindKthToTail2(node1, -2))
print(s.FindKthToTail1(node1, 2)==node3)
print(s.FindKthToTail2(node1, 2)==node3)
print('-------------------------------')
print(s.ReverseLinkls(node1)==node4)