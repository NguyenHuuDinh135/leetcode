class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_before = max(candies)
        for i in range(len(candies)):
            candies[i] += extraCandies
            if candies[i] >= max_before:
                candies[i] = True
            else:
                candies[i] = False
        return candies
        