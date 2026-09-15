# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        carry = 0
        while l1 or l2:
            if not l1:
                l1val = 0
            else:
                l1val = l1.val
            if not l2:
                l2val = 0
            else:
                l2val = l2.val
            total = l1val + l2val + carry
            if(total >= 10):
                carry = (total//10) % 10
                total = total
            else:
                carry = 0
            dummy.next = ListNode(total % 10)
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry != 0:
            dummy.next = ListNode(carry)

        return head.next  

        