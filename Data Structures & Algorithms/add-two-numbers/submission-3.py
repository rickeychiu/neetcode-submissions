# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        str1 = ""
        ptr1 = l1
        while ptr1:
            str1 += str(ptr1.val)
            ptr1 = ptr1.next
        str1 = str1[::-1] # reverse string

        str2 = ""
        ptr2 = l2
        while ptr2:
            str2 += str(ptr2.val)
            ptr2 = ptr2.next
        str2 = str2[::-1] # reverse string

        answerVal = int(str1) + int(str2)
        answerstr = str(answerVal)
        answerstr = answerstr[::-1]
        
        head = ListNode(0)
        ptr = head
        for ch in answerstr:
            ptr.next = ListNode(int(ch))
            ptr = ptr.next

        return head.next
