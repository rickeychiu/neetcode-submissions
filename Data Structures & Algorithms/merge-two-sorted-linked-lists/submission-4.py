# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None:
            return list2
        if list2 == None:
            return list1

        head = None
        ptr1 = list1
        ptr2 = list2
        if list1.val < list2.val:
            head = list1
            ptr1 = list1.next
        else:
            head = list2
            ptr2 = list2.next
        
        ptr3 = head
        
        while ptr1 != None and ptr2 != None:
            if ptr1.val > ptr2.val:
                ptr3.next = ptr2
                ptr2 = ptr2.next
                ptr3 = ptr3.next
            else:
                ptr3.next = ptr1
                ptr1 = ptr1.next
                ptr3 = ptr3.next
        
        if ptr1 != None:
            ptr3.next = ptr1
        if ptr2 != None:
            ptr3.next = ptr2

        return head


        
        