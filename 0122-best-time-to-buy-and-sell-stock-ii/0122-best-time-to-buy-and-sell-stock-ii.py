class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]: # Cái này ng ta gọi là bắt đáy nè kk
                profit += prices[i] - prices[i-1]
        return profit