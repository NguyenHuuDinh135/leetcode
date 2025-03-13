class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_money = 0
        for i in accounts:
            currentbank = sum(i)
            max_money = max(max_money, currentbank)
        return max_money
             
        