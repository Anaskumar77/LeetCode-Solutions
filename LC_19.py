# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        count = 0
        count2 = 1
        curr = head
        while curr:
            count = count + 1
            curr = curr.next

        target = count - n + 1
        if target == 1:
            return head.next

        curr = head

        while curr:
            if count2 != target-1:
                count2 += 1
                curr = curr.next
            else:
                curr.next = curr.next.next
                break  
        return head