class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(nums, target, search_left):
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    if search_left:
                        right = mid - 1
                    else:
                        left = mid + 1   
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return result
        first = binary_search(nums, target, True)
        last = binary_search(nums, target, False)
        return [first, last]