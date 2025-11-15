class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:
                lenght = 1

                while n + lenght in num_set:
                    lenght +=1
                
                longest = max(longest, lenght)
        return longest