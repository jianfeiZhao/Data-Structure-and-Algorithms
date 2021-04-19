'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:
    def deleteDuplication(self, head):
        if head == None:
            return None       
        preNode = None
        root = head
        while head.next:
            if head.value == head.next.value:
                if preNode:
                    preNode.next = head.next.next
                    if head.next.next:
                        head = head.next.next
                    else:
                        break
                else:           # at the root position
                    if head.next.next:
                        head = head.next.next
                        root = head
                    else:
                        root = preNode    #####
                        break
            else:
                preNode = head
                head = head.next
        return root
        
s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)
node6 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

root = s.deleteDuplication(node1)
while root:
    print(root.value)
    root = root.next