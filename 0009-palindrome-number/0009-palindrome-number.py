class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        dau = 0
        cuoi = -1
        if x < 0:
            return False
        list = []
        while x > 0:
            list.append(x % 10)
            x = x // 10
        if len(list) == 1:
            return True
        if len(list) == 2 and list[dau] != list[cuoi]:
            return False
        for i in range(len(list)):
            if list[i] != list[-i-1]:
                return False
        return True