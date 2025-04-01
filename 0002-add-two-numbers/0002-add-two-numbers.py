# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1 = []
        list2 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        list1.reverse()
        list2.reverse()
        num1 = ''.join(map(str, list1))
        num2 = ''.join(map(str, list2))
        result = str(int(num1) + int(num2))
        result = list(map(int, result))
        result.reverse()
        head = ListNode(result[0])
        current = head
        for i in range(1, len(result)):
            current.next = ListNode(result[i])
            current = current.next
        return head

        
            