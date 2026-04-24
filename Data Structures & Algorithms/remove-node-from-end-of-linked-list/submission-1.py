# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ind = 0
        curr = head
        cur = curr
        while cur:
            ind += 1
            cur = cur.next
        remove = ind - n
        if remove == 0:
            return curr.next
        else:
            go = 0
            while curr:
                if go + 1 == remove:
                    curr.next = curr.next.next
                    break
                else:
                    curr = curr.next
                    go += 1
            return head


        

        