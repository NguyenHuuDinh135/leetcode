class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count = {}
        res = []
        for i in nums1:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for j in nums2:
            if j in count and count[j] != 0:
                res.append(j)
                count[j] -= 1
        return res
