# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        references = []
        ptr = head
        while ptr != None:
            references.append(ptr)
            ptr = ptr.next
        
        i = 0
        j = len(references) - 1


        while i < j:

            references[i].next = references[j]
            i += 1
            references[j].next = references[i]
            j -= 1
        
        references[i].next = None