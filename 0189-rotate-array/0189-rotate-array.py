class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Nếu k lớn mảng ban đầu thì lấy phần dư để rotated
        k = k % len(nums)
        if k != 0:
        
            nums[:k], nums[k:] = nums[-k:], nums[:-k]