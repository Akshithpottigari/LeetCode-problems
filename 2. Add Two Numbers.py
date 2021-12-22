# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #           making new val for new ListNode            
            val = v1 +v2 +carry
#           getting the first digit of the val for the carrying purpose
            carry = val // 10
            val = val % 10
        
#           making a new ListNode
            current.next = ListNode(val)
            
#             updating pointers:
#             updating the current pointer
            current = current.next
            
#         updating the nodes
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        return dummy.next