class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}
        for c in s:
            if c in count_s:
                count_s[c] += 1
            else:
                count_s[c] = 1
        for c in t:
            if c in count_t:
                count_t[c] += 1
            else:
                count_t[c] = 1
        return count_s == count_t