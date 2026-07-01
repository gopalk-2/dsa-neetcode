# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        prev=None
        while node is not None:
            x=node.val
            dummy=ListNode(x)
            dummy.next=prev
            node=node.next
            prev=dummy
        return prev
   
       

        