class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:# fibonaci 1 1 2 3 5
            return n
        a = 3
        b =  2
        step = 0
        for i in range(3, n):
            step = a + b
            b = a
            a = step
        return step