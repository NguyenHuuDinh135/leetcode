class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i + 1]
            num_to_index[num] = i + 1