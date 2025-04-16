# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list= []
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1 is None and list2 is None:
            return []
        while list1 is not None:
            list.append(list1.val)
            list1 = list1.next
        while list2 is not None:    
            list.append(list2.val)
            list2 = list2.next
        list.sort()
        head = ListNode(0)
        current = head
        for i in list:
            current.next = ListNode(i)
            current = current.next
        return head.next