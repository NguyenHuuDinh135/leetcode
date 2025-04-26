class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        sum = 0

        for num in nums:
            sum += num
            max_sum = max(max_sum, sum)
            if sum < 0:
                sum = 0

        return max_sum