class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            return False

        for c in set(s):
            if s.count(c) != t.count(c): #Đếm số lần xuất hiện của char trong 2 chưỡi
                return False
        return True
        