class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        segments = split(s)
        return len(segments )