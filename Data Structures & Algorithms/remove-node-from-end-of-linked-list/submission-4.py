# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        references = []
        ptr = head
        while ptr != None:
            references.append(ptr)
            ptr = ptr.next
        
        if len(references) <= 1:
            return None
        if len(references) == 2:
            if n == 1:
                head.next = None
                return head
            elif n == 2:
                head = head.next
                return head


        removal = len(references) - n
        before = removal - 1
        after = removal + 1
        
        if before >= 0:
            references[before].next = references[removal].next
        else:
            head = head.next
        
        return head
        