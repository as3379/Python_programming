# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev


class Solution:
    def reverseList_rec(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = head.prev
            head.prev= temp
            # prev = temp
        return reverseList_rec(head.prev)
