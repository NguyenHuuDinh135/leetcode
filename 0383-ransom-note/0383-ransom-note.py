class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """ 
        count = {}
        for c in magazine:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for c in ransomNote:
            if c not in count or count[c] == 0: #count [c] == 0 có nghĩa Trường hợp hết chữ để ghép thêm
                return False
            count[c] -= 1
        return True