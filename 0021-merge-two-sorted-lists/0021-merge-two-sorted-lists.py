# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        cur1 = list1
        cur2 = list2
        res = ListNode()
        head = res

        while cur1 and cur2:
            if cur1.val >= cur2.val:
                res.next = cur2
                cur2 = cur2.next
            else:
                res.next = cur1
                cur1 = cur1.next
            res = res.next

        while cur1:
            res.next = cur1
            cur1 = cur1.next
            res = res.next

        while cur2:
            res.next = cur2
            cur2 = cur2.next
            res = res.next

        return head.next