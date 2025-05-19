class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums

        # left = 0
        # right = len(nums) - 1
        # res = [0] * len(nums)
        # for i in range(len(res) - 1, -1, -1):
        #     if abs(nums[left]) > abs(nums[right]):
        #        res[i] = nums[left] ** 2
        #        left += 1
        #     else:
        #         res[i] = nums[right] ** 2
        #         right -= 1
        # return res