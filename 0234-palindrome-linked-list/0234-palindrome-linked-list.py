# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        list = []
        while head is not None:
            list.append(head.val)
            head = head.next
        if len(list) == 1:
            return True
        if len(list) == 2 and list[0] != list[-1]:
            return False
        for i in range(len(list)):
            if list[i] != list[-i-1]:
                return False
        return True