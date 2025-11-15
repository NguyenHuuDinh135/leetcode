class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:
                cur = n
                lenght = 1
                while cur + 1 in num_set:
                    lenght +=1
                    cur +=1
                longest = max(longest, lenght)
        return longest