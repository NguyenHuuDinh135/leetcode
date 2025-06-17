class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        for i in range(len(timeSeries) - 1):
            d = timeSeries[i + 1] - timeSeries[i]
            if d > duration:
                res += duration
            else:
                res += d
        return res + duration