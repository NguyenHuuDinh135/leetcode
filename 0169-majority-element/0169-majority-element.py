class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Gặp Time Limit Exceeded
        # for i in nums:
        #     if nums.count(i) > len(nums) // 2:
        #         return i

        result = set(nums)
        return max(result, key = nums.count)