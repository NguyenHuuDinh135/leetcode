class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        list = []
        while x > 0:
            list.append(x % 10)
            x = x // 10
        if len(list) == 1:
            return True
        if len(list) == 2 and list[0] != list[-1]:
            return False
        for i in range(len(list)):
            if list[i] != list[-i-1]:
                return False
        return True