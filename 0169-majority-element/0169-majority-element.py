class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Gặp Time Limit Exceeded
        # for i in nums:// Cách 1
        #     if nums.count(i) > len(nums) // 2:
        #         return i

        # result = set(nums) //cách 2
        # return max(result, key = nums.count) O(n^2) ko tuyen tinh
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

        