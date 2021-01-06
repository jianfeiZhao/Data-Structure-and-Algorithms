'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
class Solution1:
    def printListFromTailToHead(self, listNode):
        l = []
        while listNode:
            l.insert(0, listNode.val)    # 头插法，得到链表的倒序list
            listNode = listNode.next
        return l
 
class Solution2:
    def printListFromTailToHead(self, listNode):
        l = []
        while listNode:
            l.append(listNode.val)   # 尾插法，得到链表的正序list
            listNode = listNode.next
        return l[::-1]   # 翻转输出结果

node1 = ListNode([1,2,3])
node2 = ListNode([4,5,6])
node3 = ListNode([7,8])
node4 = ListNode([9])
node1.next = node2
node2.next = node3
node3.next = node4

s = Solution1()
print(s.printListFromTailToHead(node1))
s = Solution2()
print(s.printListFromTailToHead(node1))