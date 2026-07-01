# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def get_k_node(curr,k):
    while curr and k >0:
        curr=curr.next
        k-=1
    return curr

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev_group=dummy
        
        while True:
            kth=get_k_node(prev_group,k)
            if not kth:
                break
            group_next=kth.next

            prev,curr=kth.next,prev_group.next
            while curr!=group_next:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            tmp=prev_group.next
            prev_group.next=kth
            prev_group=tmp
        return dummy.next

        