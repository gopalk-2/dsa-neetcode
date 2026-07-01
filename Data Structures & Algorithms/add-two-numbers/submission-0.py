# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp=l1
        n1=deque()
        while temp:
            n1.appendleft(temp.val)
            temp=temp.next
        n1=int(''.join(map(str,list(n1))))
        temp=l2
        n2=deque()
        
        while temp:
            n2.appendleft(temp.val)
            temp=temp.next
        n2=int(''.join(map(str,list(n2))))
        n3=str(n1+n2)
        head=None
        curr=None
        for i in range(len(n3)-1,-1,-1):
            node=ListNode(int(n3[i]))
            if i==len(n3)-1:
                head=node
                curr=node
            else:
                curr.next=node
                curr=node
        return head
        


        