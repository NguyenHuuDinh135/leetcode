class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            res[key].append(s)
        return res.values()