# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        root = ListNode(next = head)
        p1, p2 = head, root
        while n>0:
            p1 = p1.next
            n-=1
        while p1 != None:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return root.next

'''
Runtime: 24 ms, faster than 98.09% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.1 MB, less than 92.19% of Python3 online submissions for Remove Nth Node From End of List
'''