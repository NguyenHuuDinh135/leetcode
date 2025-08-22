class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        
        steps = 0
        curr_end = 0
        curr_farthest = 0
        
        for i in range(n-1):
            curr_farthest = max(curr_farthest, i + nums[i])
            if i == curr_end:
                steps += 1
                curr_end = curr_farthest
        
        return steps