class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = ""
        result = []
        for i in digits:
            sum += str(i)    
        sum = int(sum) + 1
        
        while sum > 0:
            result.append(sum % 10)
            sum = sum // 10

        result.reverse()
        return result