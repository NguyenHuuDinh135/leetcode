class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     nums[i] = nums[i] ** 2
        # nums.sort()
        # return nums

        left = 0
        right = len(nums) - 1
        res = []
        while len(res) < len(nums):
            if abs(nums[left]) > abs(nums[right]):
               res.append(nums[left] ** 2)
               left += 1
            else:
                res.append(nums[right] ** 2)    
                right -= 1
        return res[::-1]