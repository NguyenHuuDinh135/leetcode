class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle) 
        # str = haystack
        # len_haystack = len(str)

        # while str != needle:
        #     len_haystack  -= 1 
        #     if len_haystack  == 0:
        #         return -1
        # return str == needle
        