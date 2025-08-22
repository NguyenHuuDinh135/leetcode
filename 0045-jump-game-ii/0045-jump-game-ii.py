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
        end = 0
        farthest = 0
        
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                steps += 1
                break
            if i == end:
                steps += 1 
                end = farthest
        
        return steps