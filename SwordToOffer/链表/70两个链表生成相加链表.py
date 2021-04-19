'''
假设链表中每一个节点的值都在 0 - 9 之间，那么链表整体就可以代表一个整数。
给定两个这种链表，请生成代表两个整数相加值的结果链表。
例如：链表 1 为 9->3->7，链表 2 为 6->3，最后生成新的结果链表为 1->0->0->0
'''
# @param head1 ListNode类 
# @param head2 ListNode类 
# @return ListNode类
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def addInList(self , head1 , head2 ):
        # write code here
        ls1, ls2 = [], []
        while head1 or head2:
            if head1:
                ls1.append(head1.val)
                head1 = head1.next
            if head2:
                ls2.append(head2.val)
                head2 = head2.next
        vhead = ListNode(-1)
        carry = 0
        while ls1 or ls2 or carry != 0:
            # 当st1,st2都遍历完时，如果carry=0,就不需要进入循环了
            a, b = 0, 0
            if ls1:
                a = ls1.pop()
            if ls2:
                b = ls2.pop()
            get_sum = a+b+carry   #每次的和应该是对应位相加再加上进位
            ans = get_sum%10   #对累加的结果取余
            carry = get_sum//10   #如果大于0，就进位
            cur = ListNode(ans)
            cur.next = vhead.next
            vhead.next = cur   #每次把最新得到的节点更新到vhead.next中
        return vhead.next