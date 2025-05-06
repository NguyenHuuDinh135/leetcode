class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        # c1 lay dict max
        # a
        s = ""
        while count:
            a = max(count, key=count.get)
            s = s+ (a * count[a])
            del count[a]
        return s
        