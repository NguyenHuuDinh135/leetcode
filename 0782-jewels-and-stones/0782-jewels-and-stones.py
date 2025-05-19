class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = {}
        list1 = []
        for j in jewels:
            if j in count:
                count[j] += 1
            else:
                count[j] = 1
        for s in stones:
            if s in count:
                list1.append(s)
        return len(list1)
                