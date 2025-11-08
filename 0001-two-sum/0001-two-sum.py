class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}

        for i in range(0, len(nums)):
            complete = target - nums[i]
            if complete in d:
                return [d[complete], i]
            d[nums[i]] = i
        return []