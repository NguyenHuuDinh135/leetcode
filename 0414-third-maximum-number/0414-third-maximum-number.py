class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        count = 0
        if len(nums) > 3:
        # Có nghĩa là gửi về số thứ 3 lớn nhất không trùng lớn nhất
            for i in range(0, 2):
                nums.remove(max(nums))
                count += 1
                if count == 2:
                    return max(nums)
            
        if len(nums) < 3:
            return max(nums)
        if len(nums) == 3:
            return min(nums)
            
        