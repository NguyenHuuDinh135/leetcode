class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_s = 0
        s = 0
        while l < r:
            if height[l] > height[r]:
                s = height[r] * (r - l)
                r -= 1

            else:
                s = height[l] * (r - l)
                l += 1
            max_s = max(max_s, s)

        return max_s
