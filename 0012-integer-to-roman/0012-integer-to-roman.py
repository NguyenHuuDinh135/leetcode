class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        res = []

        for value, symbol in value_symbols:
            if num == 0:
                break
            count = num // value #3549 // 1000 = 3
            res.append(symbol * count) #res.append('M' * 3) "MMM"
            num -= count * value #3549 - (3 * 1000) = 549
        return ''.join(res)