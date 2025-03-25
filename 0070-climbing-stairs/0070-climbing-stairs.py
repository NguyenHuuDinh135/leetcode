class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        a = 3
        b =  2
        step = 0
        for i in range(3, n):
            step = a + b
            b = a
            a = step
        return step