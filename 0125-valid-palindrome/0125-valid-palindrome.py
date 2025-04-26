class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        list = []
        for c in s:
            if c.isalnum():
                list.append(c)
        return list == list[::-1]
        

        