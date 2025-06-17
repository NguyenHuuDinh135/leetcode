class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            while nums[nums[i]-1] != nums[i]: 
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        return [i for i in range(1, len(nums)+1) if i != nums[i-1]]