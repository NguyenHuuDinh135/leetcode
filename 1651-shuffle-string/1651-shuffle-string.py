class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        dic ={}
        res = ""
        c = 0
        for i in indices:
            dic[i] = s[c]
            c += 1
        for i in range(len(indices)):
            res += dic[i]
        return res

        