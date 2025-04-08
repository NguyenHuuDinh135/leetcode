class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for c in range(len(s)):
            if c + 1 < len(s) and roman[s[c]] < roman[s[c + 1]]:
                result -= roman[s[c]]
            else:
                result += roman[s[c]]
        return result