class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for i, num in enumerate(numbers):
            key_in_dic = target - num #Ex: complement = 9 - 2,  complement = 9 - 7 = 2
            if key_in_dic in num_to_index:
                return [num_to_index[key_in_dic], i + 1]
            num_to_index[num] = i + 1 # num_to_index = {2: 1}