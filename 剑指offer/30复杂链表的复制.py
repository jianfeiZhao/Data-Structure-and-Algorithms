'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

首先在原来链表A: {a, b, c,...}的基础上将每个节点复制一个在原节点之后A': {a, a', b, b', c, c',...}，
并复制next指针和random指针，接下来重构一个链表，只包含复制的节点 B: {a', b', c',...}
'''
class RandomListNode:
    def __init__(self, x):
        self.value = x
        self.next = None
        self.random = None
    
    def set_next(self, val):
        self.next = RandomListNode(val)

class Solution:
    def clone(self, pHead):
        if pHead == None:
            return None
        # copy a new node behind this node, copy the next pointer as well
        p = pHead
        while p != None:
            new_node = RandomListNode(p.value)
            new_node.next = p.next
            p.next = new_node
            p = new_node.next
        # copy the random pointer
        p = pHead
        while p != None:
            if p.random != None:
                p.next.random = p.random.next
            p = p.next.next
        # rebuild the linked list which only includes the copied nodes
        vhead = RandomListNode(0)  # init
        q = vhead
        p = pHead
        while p != None:
            q.next = p.next
            #p.next = p.next.next
            q = q.next
            p = p.next.next
        return vhead.next

# build a randomlinkedlist
n1 = RandomListNode(2)
n2 = RandomListNode(1)
n3 = RandomListNode(-3)
n4 = RandomListNode(4)
n1.next = n2
n2.next = n3
n2.random = n1
n3.next = n4
n3.random = n4

s = Solution()
n1_copy = s.clone(n1)
while n1_copy.next != None:
    print(n1_copy.next.value)
    if n1_copy.random != None:
        print(n1_copy.random.value) 
    print(' ')
    n1_copy = n1_copy.next

'''
True answer: 1 None | -3 2 | 4 4
'''