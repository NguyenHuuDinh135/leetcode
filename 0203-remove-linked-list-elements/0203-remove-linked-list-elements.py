# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        list1 = []
        list2 = []
        while head is not None:
            list1.append(head.val)
            head = head.next
        if list1 is None:
            return []
        for i in list1:
            if i != val:
                list2.append(i)
        if list1 is None:
            return []

        result = ListNode(0)
        current = result
        for i in list2:
            current.next = ListNode(i)
            current = current.next
        return result.next
        
        