class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0
        for i in arr1:
            check = True
            for j in arr2:
                if abs(i - j) <= d: 
                    check = False
                    break
            if check:
                count += 1
        return count